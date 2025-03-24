# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.


# #Way 1
# name=str(input("Enter your name: "))
# print("reverse of your name:",name[::-1])

#Way 2
# name=str(input("Enter your name: "))
# name=list(name)
# i=0
# j=len(name)-1
# while i<=j:
#     name[i],name[j]=name[j],name[i]
#     i+=1
#     j-=1
# print("Reversed string: ",''.join(name))

#Way 3
# name=str(input("Enter your name: "))
# rev = ''
# for char in name:
#     rev = char + rev
# print("Reversed string: ",rev)

#Way 4
# name=str(input("Enter your name: "))
# rev=''.join(reversed(name))
# print("Reversed string: ",rev)

#Way 5
#Recursion
# def reverse_string(s):
#     if len(s)==0:
#         return s
#     return reverse_string(s[1:])+s[0]
# name=str(input("Enter your name: "))
# print("Reversed string: ",reverse_string(name))

#Way 6
#Stack
name=str(input("Enter your name: "))
stack=list(name)
rev=''
while stack:
    rev += stack.pop()
print("Reversed string: ",rev)
