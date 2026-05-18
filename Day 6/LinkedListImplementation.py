# class Node:
#     def __init__(self, data):
#         self.data=data  # instance variable
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

# linkedlist = LinkedList()

# linkedlist.head=Node(5)
# second         =Node(10)
# third          =Node(15)
# fourth         =Node(20)

# #connecting nodes
# linkedlist.head.next=second
# second.next=third
# third.next=fourth 
# fourth.next=None

# # display Linked List
# while linkedlist.head != None:
#     print(linkedlist.head.data  , " ")
#     linkedlist.head=linkedlist.head.next

# Creating Dynamically
class Node:
    def __init__(self, data):
        self.data=data  # instance variable
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self, value):
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node
        else:
            self.tail.next=self.node
            self.tail     =self.node

    def display(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.next

    def addBeginning(self, value):
        self.node=Node(value)
        if self.head==None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node



if __name__== '__main__':
    Object=LinkedList()   # LinkedList object created 

    # Menu driven options
    while True:
        print("1. Add Node LinkedList: ")
        print("2. Add Node in Beginning: ")
        print("3. Add Node in Between: ")
        print("4. Add Node in End: ")
        print("5. Display LinkedList: ")
        print("6. Exists ")

        choice=int(input("Enter your choice: "))
        if choice==1:
            value=int(input("Enter the value for node: "))
            Object.addNode(value)
            print("Node added Successfully in Single LinkedList")

        elif choice==2:
            value=int(input("Enter the valur for node: "))
            Object.addBeginning(value)
            print("Node added at Beginning ")
        
        elif choice==5:
            Object.display()




