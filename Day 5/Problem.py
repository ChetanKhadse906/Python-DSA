# input=[79,77,54,81,48,34,25,16,144]
# ans=0
# for i in range(0,len(input)):
#     j=1
#     while j*j <=i:
#         if j*j==i:
#             ans+=1
#         j+=1
# print("Square Plot: ", ans)

# 1) MCQ
# def func(value, values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t, v)
# print(t, v[0])

# 2) MCQ
# def f(i, values=[]):
#     values.append(i)
#     print(values)
#     # return values
# f(1)    # calling function
# f(2)


# WAP to access each character of String in forward and backward direction by using while loop?
# input="Learning Python is very easy"
# length=len(input)
# i=0
# print("Forward direction")
# while i<length:
#     print(input[i], end=' ')
#     i=i+1
# print()
# print("Backward direction")
# i=-1
# while i>=-length:
#     print(input[i], end=' ')
#     i=i-1

# Q. 1) String 
# StringSend=str(input("Enter the String send: "))
# StringReceived=str(input("Enter the  String Received: "))
# print("String Send: ", StringSend)
# print("String Received: ", StringReceived)

# for i in range(0, len(StringSend)):
#     if StringSend[i]==StringReceived[i]:
#         continue
#     else:
#         print(StringSend[i])

# Q. 2)
# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels: ")
# # w=prashantjha
# found=[] #a 
# for i in w: 
#     if i in v:
#         if i not in found:
#             found.append(i)
# print("Found Vowels= ",found )
# print("Unique Vowels= ",len(found), "from the given word=",)

# Q. 3) Employee, Company cab service startrange, endrange
# x,y,z =map(int, input().split())
# mylist=[]
# for i in range(x):
#     a=int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
#         print(j, end=" ")

# 4) Date and Time module 
# import datetime

# datetime formatting
# date=datetime.datetime.now()
# print("It's now:{:%d%m%Y %H:%M:%S}".format(date))

# # 5)
# x=['A','B','C','D']
# y=['A','B','C','D']
# z=[1,2,3,4,]
# print(x==y)
# print(x==z)
# print(x!=z)

# 6) 
# val=[2**i for i in range(1,6)]
# print(val)

# s=[i*i for i in range(1,11)]
# print(s)

# 7) Dictionary Comprehension
# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

# 8) How to read multiple values in a single line in a list
# a, b=[int(x) for x in input("Enter 2 numbers: ").split()]
# print("Product is: ", a*b)

# 9)
# a,b,c=[float(x) for x in input("Enter 3 float number: ").split()]
# print("The Sum is: ", a+b+c)

# 10)
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased Everything")

# 11)

while True:
    Username=input("Enter Username: ")
    Password=input("Enter Password: ")

    if Username=='admin' and Password=='admin':
        print("login successfully......")
        break
    else:
        print("Invalid")
        