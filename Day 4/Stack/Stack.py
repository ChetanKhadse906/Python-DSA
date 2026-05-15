# Stack Implementation 
# Two ways
# 1) List/ Array     ----> for small amount of data
# 2) Linked List     ----> for large amount of data

# Stack Operations
# 1) Push 
# 2) Pop 
# 3) Peek  
# 4) isEmpty
# 5) isFull
# 6) Delete
# 7) display

#  (I) Without size
# import sys
# class Stack:
#     def __init__(self):
#         self.myStack=[]

#     def push(self, value):
#         self.myStack.append(value)
#         print("Element is Pushed")

#     def display(self):
#         print(self.myStack)
    
#     def isEmpty(self):
#         if self.myStack==[]:
#             return True
#         else:
#             return False

#     def pop(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack.pop())
#             print("Element is Popped")

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is Empty")
#         else:
#             print(self.myStack[-1])

#     def deleteStack(self):
#         self.myStack=None


# obj=Stack()
# print("Stack has created: ")

# while True:
#     print("1. Push Operation: ")
#     print("2. Display Stack: ")
#     print("3. Pop Operation: ")
#     print("4. Peek Operation: ")
#     print("5. delete Stack: ")
#     print("7. Exist")
#     choice=int(input("Enter Your Choice: "))
#     if choice==1:
#         value=int(input("Enter value to push in Stack: "))
#         obj.push(value)
#     elif choice==2:
#         obj.display()
#     elif choice==3:
#         obj.pop()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.deleteStack()
#     else:
#         sys.exist()


# (II) with size 
import sys
class Stack:
    def __init__(self, size):
        self.myStack=[]
        self.stackSize=size
    
    def isFull(self):
        if len(self.myStack)==self.stackSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            print("Stack is Full")
        else:
            self.myStack.append(value)
            print("Element is Pushed")

    def display(self):
        print(self.myStack)
    
    def isEmpty(self):
        if self.myStack==[]:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack.pop())
            print("Element is Popped")

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.myStack[-1])

    def deleteStack(self):
        self.myStack=[]

size=int(input("Enter the size of Stack: "))
obj=Stack(size)
print("Stack has created: ")

while True:
    print("1. Push Operation: ")
    print("2. Display Stack: ")
    print("3. Pop Operation: ")
    print("4. Peek Operation: ")
    print("5. delete Stack: ")
    print("7. Exist")
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        value=int(input("Enter value to push in Stack: "))
        obj.push(value)
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.deleteStack()
    else:
        sys.exist()
