#Implementing the singly linked list 

class sllist:
    class node:
        def __init__(self,data):
            self.element=data
            self.next=None
    def __init__(self):
        self.size=0
        self.head=self.node(None)
        
    #returns the size of list     
    def listsize(self):
        return self.size
    
    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node
    #inserts element at the first of the list 
    def insertFirst(self,data):
        newNode=self.node(data)
        if self.size==0:
            self.head.element=newNode.element
            newNode.next=None
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1
    
    #inserts the element at the last of the list
    def insertLast(self,data):
        newNode=self.node(data)
        if self.size==0:
            self.head.element=newNode.element
            newNode.next=None
        else:
            currentNode=self.head
            while(currentNode.next!=None):
                currentNode=currentNode.next
            currentNode.next=newNode
        self.size+=1

    #deletes the element at the first of the list
    def deleteFirst(self):
        if self.size==0:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            del temp
        self.size-=1
    
    #deletes the last element in the list
    def deleteLast(self):
        if self.size==0:
            print("List is empty")
        elif self.size==1:
            self.head=self.node(None)
            self.size=0
        else:
            currentNode=self.head
            while(currentNode):
                if currentNode.next.next==None:
                    currentNode.next=None
                currentNode=currentNode.next
            self.size-=1
    def printList(self):
        if self.size==0:
            print("List is empty")
        else:
            currentNode=self.head
            while(currentNode!=None):
                print(currentNode.element,end=" ")
                currentNode=currentNode.next
            print(" ")

    #inserts the element e after pth node
    def insertAfter(self,p,e):
        newNode=self.node(e)
        if self.size==0:
            self.head.element=newNode.element
        elif (self.size==1):
            self.insertLast(e)
        else:
            currentNode=self.head
            index=0
            while(currentNode):
                if index==p:
                    newNode.next=currentNode.next
                    currentNode.next=newNode
                    return True
                currentNode=currentNode.next
                index+=1
        self.size+=1

    #insert the element e before pth node
    def insertBefore(self,p,e):
        newNode=self.node(e)
        if self.size==0:
            self.head.element=newNode.element
        elif self.size==1:
            self.insertFirst(e)
        else:
            currentNode=self.head
            index=0
            while(currentNode):
                if index==p-1:
                    newNode.next=currentNode.next
                    currentNode.next=newNode
                    return True
                currentNode=currentNode.next
                index+=1
        self.size+=1

    #deletes the element after pth node    
    def deleteAfter(self,p):
        if self.size==0:
            print("List is empty")
        elif self.size==1:
            self.deleteFirst()
            self.size-=1
        else:
            currentNode=self.head
            index=0
            while(currentNode):
                if index==p:
                    currentNode.next=currentNode.next.next
                    return True
                currentNode=currentNode.next
                index+=1
            self.size-=1


    #delete the element before pth node    
    def deleteBefore(self,p):
        if self.size==0:
            print("List is empty")
        elif self.size==1:
            self.deleteFirst()
            self.size-=1
        else:
            currentNode=self.head
            index=0
            while(currentNode):
                if index==p-2:
                    currentNode.next=currentNode.next.next
                    return True
                currentNode=currentNode.next
                index+=1
            self.size-=1
    
    #delete the element at pth node
    def deletepthnode(self,p):
        if self.size==0:
            print("list is empty")
        else:
            if self.head.next==None:
                self.deleteFirst() # or deleteLast
            else:
                index=0
                currentNode=self.head
                while(currentNode):
                    if index==p-1:
                        temp=currentNode.next
                        currentNode.next=currentNode.next.next
                        del temp
                        return True
                    currentNode=currentNode.next
                    index+=1
            self.size-=1

    #Swapping the elements in p and q nodes 
    def swapElement(self, p, q):
        if p < 0 or q < 0 or p >= self.size or q >= self.size:
            return False  # Invalid positions

        current_node_p = self.head
        current_node_q = self.head
        index_p = 0
        index_q = 0

        while current_node_p and index_p < p:
            current_node_p = current_node_p.next
            index_p += 1

        while current_node_q and index_q < q:
            current_node_q = current_node_q.next
            index_q += 1

        # temp = current_node_p.element
        # current_node_p.element = current_node_q.element
        # current_node_q.element = temp
        current_node_p.element,current_node_q.element = current_node_q.element,current_node_p.element

        return True
    
    #Replacing the element in pth node with element e
    def replace(self,p,e):
        currentnode=self.head
        index=0
        while(currentnode):
            if index==p:
                currentnode.element=e
                break
            currentnode=currentnode.next
            index+=1
    # Removing nth node from end using slow and fast poninters with constant space complexity 
    def removeNthFromEnd(self, head, n):
        temp=head
        slow=temp
        fast=temp
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return temp.next

sl=sllist()
sl.insertFirst(50)
sl.insertFirst(40)
sl.insertFirst(30)
sl.insertFirst(20)
sl.insertFirst(10)
sl.printList()

