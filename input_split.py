li=[]
n=int(input())
while(n>0):
    command=input()
    operation=command.split()
    if(operation[0]=="insert"):
        li.insert(int(operation[1]),int(operation[2])) 
    
    elif(operation[0]=="remove"):
        li.remove(int(operation[1]))
    
    elif(operation[0]=="append"):
        li.append(int(operation[1]))
    
    elif(operation[0]=="print"):
        print(li)
    elif(operation[0]=="sort"):
        li.sort()
    elif(operation[0]=="pop"):
        li.pop()
    elif(operation[0]=="reverse"):
        li.reverse()
    n-=1
