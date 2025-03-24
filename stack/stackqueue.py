class mystack():
    def __init__(self,size):
        self.s=[]
        self.max=size
        self.top=-1
        self.sz=0
        for i in range(self.max):
            self.s.append(None)
    def size(self):
        return self.top+1
    def isempty(self):
        return self.top<0
    def push(self,item):
        if self.sz==self.max:
            print("Stack full exception")
        else:
            self.top+=1
            self.s[self.top]=item
        self.sz+=1
    def pop(self):
        if self.sz==0:
            print("Stack empty exception")
        else:
            obj=self.s[self.top]
            self.s[self.top]=None
            self.top-=1
            return obj
        self.sz-=1
    def isempty(self):
        if (self.sz==0):
            return 1
    def isfull(self):
        if(self.sz==self.max):
            return 1
    def printstack(self):
        for i in range(self.size()):
            if(self.s[i]!=None):
                print(self.s[i],end=" ")
        print(" ")


class myqueue():
    def __init__(self,size):
        self.max=size
        self.f=0
        self.r=-1
        self.sz=0
        self.q=[]
        for i in range(self.max):
            self.q.append(None)
    def size(self):
        return self.sz
    def enqueue(self,item):
        if self.sz==self.max:
            print("Queue full exception")
        else:
            self.r=(self.r+1)%self.max
            self.q[self.r]=item
        self.sz+=1
    def dequeue(self):
        if self.sz==0:
            print("queue empty exception")
        else:
            self.f=(self.f-1)%self.max
            self.q[self.f]=None
        self.sz-=1
    def isempty(self):
        if self.sz==0:
            return 1
    def isfull(self):
        if self.sz==self.max:
            return 1
    def printqueue(self):
        for i in range(self.sz):
            if(self.q[i]!=None):
                print(self.q[i],end=" ")
        print(" ")
    def getfront(self):
        return self.q[self.f]
    def getrear(self):
        return self.q[self.r]
string=input()
string.strip()
lst=[]
for letter in string:
    if letter!=" ":        
        lst.append(letter)
# print(lst)
s1=mystack(len(lst))
q1=myqueue(len(lst))
for i in range(len(lst)):
    s1.push(lst[i])
    q1.enqueue(lst[i])
flag=0
for i in range(s1.size()):
    if s1.pop()!=q1.dequeue():
        flag=0
    else:
        flag=1
if flag==1:
    print("palidrome")
else:
    print("Not a palindrome")