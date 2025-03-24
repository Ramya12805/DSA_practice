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


#with 3 stacks s1,s2,s3 
#s1 is intial stack 
# copy s1 into s2
# then pop all elements from s1 and push them into s3
# then one by one pop elements from s2 and s3 and check each element 
string=input()
lst=[]

for i in string:
    if i!=" ":
        lst.append(i)

s1=mystack(len(lst))
for i in range(len(lst)):
    s1.push(lst[i])

s2=mystack(s1.size())
k=s1.size()
flag=0
for i in range(k//2):
    s2.push(s1.pop())
if k%2==0:
    for i in range(k//2):
        if s1.pop()==s2.pop():
            flag=1
        else:
            flag=0
elif k%2!=0:
    s1.pop()
    for i in range(k//2):
        if s1.pop()==s2.pop():
            flag=1
        else:
            flag=0

if flag==1:
    print("palindrome")
else:
    print("Not a palindrome")