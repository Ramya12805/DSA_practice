class sllist:
    class node:
        def __init__(self,data):
            self.element=data
            self.next=None
    def __init__(self):
        self.size=0
        self.head=self.node(None)
    def listsize(self):
        return self.size
    def insertFirst(self,data):
        newNode=self.node(data)
        if self.size==0:
            self.head.element=newNode.element
            newNode.next=None
        else:
            newNode.next=self.head
            self.head=newNode
        self.size+=1
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
    def deleteFirst(self):
        if self.size==0:
            print("List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            del temp
        self.size-=1
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

sl=sllist()
sl.insertFirst(30)
sl.insertLast(40)
sl.printList()
sl.deleteFirst()
sl.printList()
sl.deleteLast()
sl.printList()