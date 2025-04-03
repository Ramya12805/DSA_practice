package main
import (
    "fmt"
    "math/rand"
    "sync"
    "time"
)
type MessageType string
const (
    REQUEST   MessageType = "REQUEST"
    REPLY     MessageType = "REPLY"
    HEARTBEAT MessageType = "HEARTBEAT"
)
type Message struct {
    timestamp int
    senderID  int
    typeMsg   MessageType
    priority  int // Added priority field
}
type ProcessState string
const (
    IDLE       ProcessState = "IDLE"
    REQUESTING ProcessState = "REQUESTING"
    IN_CS      ProcessState = "IN-CS"
)
type Process struct {
    id                int
    timestamp         int
    clock             int
    deferred          map[int]bool
    mutex             sync.Mutex
    cond              *sync.Cond
    replyCount        int
    requestingCS      bool
    status            ProcessState
    priority          int               // Process priority for resolving conflicts
    lastHeartbeat     map[int]time.Time // Track last heartbeat from each process
    failedProcesses   map[int]bool      // Track known failed processes
    messageQueue      map[int][]Message // Queue messages from each process
    requestTimeout    time.Duration     // Timeout for request messages
    heartbeatInterval time.Duration     // Interval for sending heartbeats
    heartbeatTimeout  time.Duration     // Timeout for considering a process failed
    deadlockTimeout   *time.Timer       // Timer for detecting potential deadlocks
    waitStart         time.Time         // When the process started waiting
    requestAttempts   int               // Number of request attempts (for exponential backoff)
}
var (
    processes      []*Process
    totalProcesses = 5
    rounds         = 2 // Number of CS attempts per process
    wg             sync.WaitGroup
)
// Initialize a new process
func NewProcess(id int) *Process {
    p := &Process{
        id:                id,
        clock:             0,
        status:            IDLE,
        deferred:          make(map[int]bool),
        priority:          rand.Intn(100), // Initial random priority
        lastHeartbeat:     make(map[int]time.Time),
        failedProcesses:   make(map[int]bool),
        messageQueue:      make(map[int][]Message),
        requestTimeout:    2 * time.Second,
        heartbeatInterval: 500 * time.Millisecond,
        heartbeatTimeout:  2 * time.Second,
        requestAttempts:   0,
    }
    p.cond = sync.NewCond(&p.mutex)
    return p
}
// Start heartbeat sender
func (p *Process) startHeartbeat() {
    go func() {
        for {
            // Send heartbeat to all other processes
            for _, other := range processes {
                if other.id != p.id {
                    go other.receiveMessage(Message{
                        timestamp: p.clock,
                        senderID:  p.id,
                        typeMsg:   HEARTBEAT,
                    })
                }
            }
            time.Sleep(p.heartbeatInterval)
        }
    }()
}

// Start failure detector
func (p *Process) startFailureDetector() {
    go func() {
        ticker := time.NewTicker(p.heartbeatInterval)
        defer ticker.Stop()
        for range ticker.C {
            p.detectFailures()
        }
    }()
}
// Detect failed processes based on heartbeat timeout
func (p *Process) detectFailures() {
    p.mutex.Lock()
    defer p.mutex.Unlock()


    now := time.Now()
    for id, lastTime := range p.lastHeartbeat {
        if now.Sub(lastTime) > p.heartbeatTimeout && !p.failedProcesses[id] {
            p.failedProcesses[id] = true
            fmt.Printf("[FAILURE-DETECTION] P%d detected failure of P%d (no heartbeat for %v)\n",
                p.id, id, p.heartbeatTimeout)


            // If waiting for replies and this process hasn't replied yet,
            // count it as a reply to avoid waiting indefinitely
            if p.status == REQUESTING && p.replyCount < totalProcesses-1 {
                p.replyCount++
                fmt.Printf("[FAILURE-HANDLING] P%d no longer waiting for reply from failed P%d (%d/%d replies)\n",
                    p.id, id, p.replyCount, totalProcesses-1-len(p.failedProcesses))


                if p.replyCount >= totalProcesses-1-len(p.failedProcesses) {
                    fmt.Printf("[FAILURE-HANDLING] P%d has enough replies now, can proceed\n", p.id)
                    p.cond.Broadcast()
                }
            }
        }
    }
}
// Send a request to enter the critical section
func (p *Process) sendRequest() {
    p.mutex.Lock()
    p.clock++
    p.timestamp = p.clock
    p.requestingCS = true
    p.replyCount = 0
    p.status = REQUESTING
    p.requestAttempts++
    p.waitStart = time.Now()
    // Start deadlock detection timer
    if p.deadlockTimeout != nil {
        p.deadlockTimeout.Stop()
    }
    // Use exponential backoff for timeout
    timeout := p.requestTimeout * time.Duration(1<<uint(p.requestAttempts-1))
    if timeout > 10*time.Second {
        timeout = 10 * time.Second // Cap at 10 seconds
    }
    p.deadlockTimeout = time.AfterFunc(timeout, func() {
        p.handlePotentialDeadlock()
    })
    fmt.Printf("\n[REQUEST-START] P%d requesting CS with timestamp=%d, priority=%d\n",
        p.id, p.timestamp, p.priority)
    fmt.Printf("[REQUEST-DETAILS] P%d state=%s, clock=%d, attempt=%d\n",
        p.id, p.status, p.clock, p.requestAttempts)
    // Check for active peers
    activePeers := 0
    for _, other := range processes {
        if other.id != p.id && !p.failedProcesses[other.id] {
            activePeers++
        }
    }
    fmt.Printf("[REQUEST-PEERS] P%d found %d active peers out of %d total\n",
        p.id, activePeers, totalProcesses-1)

    p.mutex.Unlock()
    // Send REQUEST messages to all other non-failed processes
    for _, other := range processes {
        if other.id != p.id {
            p.mutex.Lock()
            if !p.failedProcesses[other.id] {
                p.mutex.Unlock()
                fmt.Printf("[REQUEST-SEND] P%d sending REQUEST to P%d\n", p.id, other.id)
                go other.receiveMessage(Message{
                    timestamp: p.timestamp,
                    senderID:  p.id,
                    typeMsg:   REQUEST,
                    priority:  p.priority,
                })
            } else {
                p.mutex.Unlock()
            }
        }
    }
    // Wait for replies from all other active processes
    p.mutex.Lock()
    defer p.mutex.Unlock()
    activePeers = totalProcesses - 1 - len(p.failedProcesses)
    fmt.Printf("[REQUEST-WAIT] P%d waiting for %d replies\n", p.id, activePeers)
    for p.replyCount < activePeers {
        fmt.Printf("[REQUEST-WAIT] P%d has %d/%d replies, waiting...\n",
            p.id, p.replyCount, activePeers)
        p.cond.Wait()
        // Recalculate active peers in case more failures were detected while waiting
        newActivePeers := totalProcesses - 1 - len(p.failedProcesses)
        if newActivePeers != activePeers {
            fmt.Printf("[REQUEST-WAIT] P%d recalculated active peers: %d -> %d\n",
                p.id, activePeers, newActivePeers)
            activePeers = newActivePeers
        }
    }
    // Stop deadlock detection timer
    if p.deadlockTimeout != nil {
        p.deadlockTimeout.Stop()
        p.deadlockTimeout = nil
    }
    p.status = IN_CS
    waitTime := time.Since(p.waitStart)
    fmt.Printf("[CS-ENTER] P%d entering Critical Section (waited %v)\n", p.id, waitTime)
    fmt.Printf("[CS-STATS] P%d timestamp=%d, priority=%d, replies=%d/%d\n",
        p.id, p.timestamp, p.priority, p.replyCount, activePeers)
    // Simulate work inside CS
    go func() {
        time.Sleep(time.Millisecond * 500)
        p.exitCS()
    }()
}


// Handle a potential deadlock
func (p *Process) handlePotentialDeadlock() {
    p.mutex.Lock()
    defer p.mutex.Unlock()


    if p.status != REQUESTING {
        return // No longer requesting, nothing to do
    }


    fmt.Printf("\n[DEADLOCK-DETECTED] P%d potential deadlock after waiting %v\n",
        p.id, time.Since(p.waitStart))
    fmt.Printf("[DEADLOCK-STATUS] P%d has %d/%d replies, status=%s\n",
        p.id, p.replyCount, totalProcesses-1-len(p.failedProcesses), p.status)


    // Increase priority significantly to break deadlock
    oldPriority := p.priority
    p.priority += 100 + rand.Intn(50)


    // Reset request state
    p.requestingCS = false
    p.status = IDLE


    // Release any deferred replies
    deferredCount := len(p.deferred)
    for id := range p.deferred {
        delete(p.deferred, id)
    }


    // Broadcast to wake up any waiting goroutines
    p.cond.Broadcast()


    fmt.Printf("[DEADLOCK-RESOLUTION] P%d backing off and retrying with higher priority\n", p.id)
    fmt.Printf("[DEADLOCK-DETAILS] P%d priority: %d -> %d, cleared %d deferred replies\n",
        p.id, oldPriority, p.priority, deferredCount)


    // Try again after a short delay
    go func() {
        backoffTime := time.Duration(100+rand.Intn(200)) * time.Millisecond
        fmt.Printf("[DEADLOCK-RETRY] P%d waiting %v before retrying\n", p.id, backoffTime)
        time.Sleep(backoffTime)
        p.sendRequest()
    }()
}


// Process received messages
func (p *Process) receiveMessage(msg Message) {
    p.mutex.Lock()
    defer p.mutex.Unlock()
    // Update logical clock
    oldClock := p.clock
    p.clock = max(p.clock, msg.timestamp) + 1
    // Update heartbeat timestamp
    p.lastHeartbeat[msg.senderID] = time.Now()
    // Clear failed status if previously marked as failed
    if p.failedProcesses[msg.senderID] {
        delete(p.failedProcesses, msg.senderID)
        fmt.Printf("[RECOVERY] P%d detected P%d is back online\n", p.id, msg.senderID)
    }
    switch msg.typeMsg {
    case REQUEST:
        fmt.Printf("[REQUEST-RECEIVED] P%d received REQUEST from P%d\n", p.id, msg.senderID)
        fmt.Printf("[REQUEST-DETAILS] timestamp=%d, priority=%d (my clock: %d -> %d)\n",
            msg.timestamp, msg.priority, oldClock, p.clock)
        shouldDefer := false
        deferReason := ""


        // Check if we should defer the reply
        if p.status == IN_CS {
            shouldDefer = true
            deferReason = "I'm in critical section"
        } else if p.status == REQUESTING {
            // Compare by timestamp first
            if msg.timestamp > p.timestamp {
                shouldDefer = false
                deferReason = "My timestamp is lower"
            } else if msg.timestamp < p.timestamp {
                shouldDefer = true
                deferReason = "Their timestamp is lower"
            } else {
                // If timestamps are equal, use priority
                if msg.priority < p.priority {
                    shouldDefer = false
                    deferReason = "My priority is higher"
                } else if msg.priority > p.priority {
                    shouldDefer = true
                    deferReason = "Their priority is higher"
                } else {
                    // If priorities are equal, use process ID
                    shouldDefer = msg.senderID > p.id
                    if shouldDefer {
                        deferReason = "Equal priority, their ID is higher"
                    } else {
                        deferReason = "Equal priority, my ID is higher"
                    }
                }
            }
        }


        if shouldDefer {
            // Defer reply
            if !p.deferred[msg.senderID] {
                p.deferred[msg.senderID] = true
                fmt.Printf("[REPLY-DEFERRED] P%d defers reply to P%d (%s)\n",
                    p.id, msg.senderID, deferReason)
            }
        } else {
            // Send reply immediately
            p.clock++
            fmt.Printf("[REPLY-IMMEDIATE] P%d sends reply to P%d (%s)\n",
                p.id, msg.senderID, deferReason)
            go processes[msg.senderID].receiveMessage(Message{
                timestamp: p.clock,
                senderID:  p.id,
                typeMsg:   REPLY,
            })
        }


    case REPLY:
        fmt.Printf("[REPLY-RECEIVED] P%d received REPLY from P%d\n", p.id, msg.senderID)


        if p.status == REQUESTING {
            p.replyCount++
            activePeers := totalProcesses - 1 - len(p.failedProcesses)
            fmt.Printf("[REPLY-COUNT] P%d now has %d/%d replies\n",
                p.id, p.replyCount, activePeers)


            if p.replyCount >= activePeers {
                fmt.Printf("[REPLY-COMPLETE] P%d has all required replies\n", p.id)
                p.cond.Broadcast() // Notify waiting process
            }
        } else {
            fmt.Printf("[REPLY-IGNORED] P%d ignoring reply (not requesting CS)\n", p.id)
        }


    case HEARTBEAT:
        // Just update the timestamp (already done above)
        // No output to reduce noise
    }
}


// Exit the critical section
func (p *Process) exitCS() {
    p.mutex.Lock()
    defer p.mutex.Unlock()


    fmt.Printf("\n[CS-EXIT] P%d exiting Critical Section\n", p.id)
    p.requestingCS = false
    p.status = IDLE
    p.requestAttempts = 0 // Reset retry counter


    // Reply to deferred requests
    deferredCount := len(p.deferred)
    fmt.Printf("[CS-EXIT-DEFERRED] P%d has %d deferred replies to send\n",
        p.id, deferredCount)


    for deferredID := range p.deferred {
        delete(p.deferred, deferredID)
        if !p.failedProcesses[deferredID] {
            p.clock++
            fmt.Printf("[DEFERRED-REPLY] P%d sending deferred reply to P%d\n",
                p.id, deferredID)
            go processes[deferredID].receiveMessage(Message{
                timestamp: p.clock,
                senderID:  p.id,
                typeMsg:   REPLY,
            })
        } else {
            fmt.Printf("[DEFERRED-SKIP] P%d skipping deferred reply to failed P%d\n",
                p.id, deferredID)
        }
    }


    fmt.Printf("[CS-EXIT-COMPLETE] P%d is now IDLE\n", p.id)
}


// Utility function to get maximum of two integers
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}


// Run the simulation
func simulation() {
    fmt.Println("========== RICART-AGRAWALA ALGORITHM SIMULATION ==========")
    fmt.Printf("Total processes: %d, Rounds per process: %d\n\n", totalProcesses, rounds)


    // Initialize processes
    fmt.Println("1. INITIALIZATION PHASE")
    for i := 0; i < totalProcesses; i++ {
        processes = append(processes, NewProcess(i))
        fmt.Printf("   Created P%d with initial priority %d\n", i, processes[i].priority)
    }


    // Start heartbeats and failure detectors
    fmt.Println("\n2. STARTING HEARTBEAT AND FAILURE DETECTION")
    for _, p := range processes {
        p.startHeartbeat()
        p.startFailureDetector()
        fmt.Printf("   P%d started heartbeat (interval: %v) and failure detection\n",
            p.id, p.heartbeatInterval)
    }


    // Wait a bit to establish heartbeats
    fmt.Println("\n3. ESTABLISHING HEARTBEAT NETWORK")
    time.Sleep(time.Millisecond * 500)
    fmt.Println("   Heartbeat network established")


    // Start process simulations
    fmt.Println("\n4. STARTING SIMULATION")
    for i := 0; i < totalProcesses; i++ {
        wg.Add(1)
        go func(p *Process) {
            defer wg.Done()
            for j := 0; j < rounds; j++ {
                // Random delay before next request
                delay := rand.Intn(1500) + 500
                time.Sleep(time.Duration(delay) * time.Millisecond)
                p.sendRequest()
            }
        }(processes[i])
    }


    // Simulate a random process failure after some time
    go func() {
        time.Sleep(time.Second * 2)
        failedID := rand.Intn(totalProcesses)
        fmt.Printf("\n[FAILURE-SIMULATION] Simulating failure of process P%d\n", failedID)
        // We don't actually stop the process, just stop its heartbeats
        // Other processes will detect the failure via timeout
        processes[failedID] = NewProcess(failedID) // Replace with non-participating process
        fmt.Printf("[FAILURE-SIMULATION] P%d is now silent (not sending heartbeats)\n", failedID)
    }()


    // Wait for all processes to complete their rounds
    wg.Wait()
    fmt.Println("\n========== SIMULATION COMPLETED ==========")
}


func main() {
    rand.Seed(time.Now().UnixNano())
    simulation()
}


