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

    def addBeginning(self, value):
        self.node=Node(value)
        if self.head==None:
            self.head=self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node

    def addNodeBetween(self, value, index):
        self.node = Node(value)

        # If Linked List is empty
        if self.head is None:
            self.head = self.node
            self.tail = self.node

        # Insert at beginning
        elif index == 0:
            self.node.next = self.head
            self.head = self.node

        # Insert in between
        else:
            temp = self.head
            count = 0

        # Move temp to node before required index
        while count < index - 1 and temp is not None:
            temp = temp.next
            count += 1

            # Insert node
            self.node.next = temp.next
            temp.next = self.node

            # If inserted at last position
            if self.node.next is None:
                self.tail = self.node

    def display(self):
        while self.head!=None:
            print(self.head.data)
            self.head=self.head.next

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
            value=int(input("Enter the value for node: "))
            Object.addBeginning(value)
            print("Node added at Beginning ")
        
        elif choice==3:
            value=int(input("Enter the value for node:  "))
            index=int(input("Enter the index at which you want to insert node: "))
            Object.addNodeBetween(value,index)
            print("Node added in Between")
        
        elif choice==5:
            Object.display()




