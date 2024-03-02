#Implementing doubly linked list
class dllist:
    class node:
        def _init_(self, data):
            self.element = data
            self.prev = None
            self.next = None
    
    def _init_(self):
        self.head = self.node(None)
        self.tail = self.node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def insertFirst(self, data):
        newNode = self.node(data)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1
    
    def insertLast(self, data):
        newNode = self.node(data)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def deleteFirst(self):
        if self.size == 0:
            print("list is empty")
        else:
            temp = self.head.next
            temp.next.prev = self.head
            self.head.next = temp.next
            del temp
            self.size -= 1

    def deleteLast(self):
        if self.size == 0:
            print("list is empty")
        else:
            temp = self.tail.prev
            temp.prev.next = self.tail
            self.tail.prev = temp.prev
            del temp
            self.size -= 1

    def printList(self):
        if self.size == 0:
            print("list is empty")
        else:
            currentNode = self.head.next
            while currentNode != self.tail:
                print(currentNode.element, end=" ")
                currentNode = currentNode.next
            print(" ")

# Example usage:
dll = dllist()
dll.insertFirst(10)
dll.insertFirst(20)
dll.insertLast(30)
dll.printList()  # Output: 20 10 30
dll.deleteFirst()
dll.printList()  # Output: 10 30
dll.deleteLast()
dll.printList()  # Output: 10
