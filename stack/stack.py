class mystack:
    def __init__(self,size):
        self.s=[]
        self.max=size
        self.top=-1
        for i in range(size):
            self.s.append(None)
    def isempty(self):
        return self.top<0
    def size(self):
        return self.top+1
    def printstack(self):
        if(self.isempty()):
            print("stack is empty")
        else:
            for i in range(self.max):
                if(self.s[i]!=None):
                    print(self.s[i],end=" ")
            print(" ")
    def push(self,item):
        self.top+=1
        self.s[self.top]=item
    def pop(self):
        if(not(self.isempty())):
            self.s[self.top]=None
            self.top-=1
        else:
            print("Stack is empty")
    def topelement(self):
        print(self.s[self.top])
s1=mystack(5)
s1.isempty()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
d=s1.size()
print(d)
s1.printstack()
s1.topelement()
s1.pop()
s1.pop()
s1.printstack()
s1.topelement()


# class mystack():
#     def __init__(self,size):
#         self.s=[]
#         self.max=size
#         self.top=-1
#         self.sz=0
#         for i in range(self.max):
#             self.s.append(None)
#     def size(self):
#         return self.top+1
#     def isempty(self):
#         return self.top<0
#     def push(self,item):
#         if self.sz==self.max:
#             print("Stack full exception")
#         else:
#             self.top+=1
#             self.s[self.top]=item
#         self.sz+=1
#     def pop(self):
#         if self.sz==0:
#             print("Stack empty exception")
#         else:
#             obj=self.s[self.top]
#             self.s[self.top]=None
#             self.top-=1
#             return obj
#         self.sz-=1
#     def isempty(self):
#         if (self.sz==0):
#             return 1
#     def isfull(self):
#         if(self.sz==self.max):
#             return 1
#     def printstack(self):
#         for i in range(self.size()):
#             if(self.s[i]!=None):
#                 print(self.s[i],end=" ")
#         print(" ")