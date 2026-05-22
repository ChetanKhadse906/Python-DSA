# Queue Implementation

# Operation                Time Complexity       Space Complexity
# Create Queue              O(1)                  O(1)
# Enqueue                   O(n)                  O(1)
# Deqeue                    O(n)                  O(1)
# Peek                      O(1)                  O(1)
# isEmpty                   O(1)                 O(1)
# Delete Entire Queue       O(1)                 O(1)

# --Queue using List
# -Easy to Implement
# -Speed problem when it grows

# --Queue using Linked List
# -Fast Performance
# -Implementation is not easy

# Queue Operation
# 1) EnQueue
# 2) DeQueue
# 3) Display Queue
# 4) isEmpty()
# 5) isFull()
# 6) delete
# 7) peek 

# with size
import sys
class Queue:
    def __init__(self, size):
        self.myQueue=[]
        self.queueSize=size

    def isFull(self):
        if len(self.myQueue)==size:
            return True
        else:
            return False

    def Enqueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.myQueue.append(value)
            print("Element is added in Queue Successfully.....")

    def Display(self):
        print(self.myQueue)

    def isEmpty(self):
        if self.myQueue==[]:
            return True
        else:
            return False

    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            self.myQueue.pop(0)
            print("Element is deleted from Queue")

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue[0])

    def deleteQueue(self):
        # self.myQueue=[]
         del self.myQueue

size=int(input("Enter the size of Queue: "))
obj=Queue(size)
print("Stack has Created: ")

while True:
    print("1. Enqueue Operation: ")
    print("2. Display Queue: ")
    print("3. Dequeue Operation: ")
    print("4. Peek Operation: ")
    print("5. Delete Queue: ")
    print("6. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        value=int(input("Enter the element: "))
        obj.Enqueue(value)
    elif choice==2:
        obj.Display()
    elif choice==3:
        obj.Dequeue()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.deleteQueue()
    elif choice==6:
        sys.exit()
    
   

