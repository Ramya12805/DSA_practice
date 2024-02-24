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

num=int(input())
q=""
while(num>0):
    r=num%16
    if r==10:
        q+='A'
    elif r==11:
        q+='B'
    elif r==12:
        q+='C'
    elif r==13:
        q+='D'
    elif r==14:
        q+='E'
    elif r==15:
        q+='F'
    else:
        q+=str(r)
    num=num//16
s1=mystack(len(q))
for i in q:
    s1.push(i)
s2=mystack(s1.size())
for i in range(s1.size()):
   s2.push(s1.pop())
s2.printstack()