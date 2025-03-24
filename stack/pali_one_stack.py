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


string=input()
lst=[]
str2=""
for i in string:
    if i!=" ":
        lst.append(i)
        str2+=i
s1=mystack(len(lst))
for i in range(len(lst)):
    s1.push(lst[i])
s1.printstack()
str1=""
for i in range(s1.size()):
    p=s1.pop()
    str1+=str(p)
if str2==str1:
    print("Palindrome")
else:
    print("not a palindrome")
