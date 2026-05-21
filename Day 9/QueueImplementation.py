# Queue Impplementation Using Linked List 
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

    # def __str__(self):
    #     return str(self.value)

    #     while curNode:
    #         yield curNode 
    #         curNode=curNode.next 

class LinkedList:
    def __init__(self):
        self.head=None
        self.til=None

class Queue:
    def __init__(self):
        self.linkedlist=LinkedList()

    # def __str__(self):
    #     values=[str(x) for x in self.linkedlist]
    #     return ' '.join(values)

    def enQueue(self, value):
        newNode=Node(value)
        if self.linkedlist.head==None:
            self.linkedlist.head=newNode
            self.linkedlist.tail=newNode 
        else:
            self.linkedlist.tail.next=newNode
            self.linkedlist.tail=newNode

    def isEmpty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False

    def deQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            tempNode=self.linkedlist.head

            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next 
                return tempNode.value

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            nodeValue=self.linkedlist.head.value
            return nodeValue

    def Display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            temp=self.linkedlist.head

            while temp!=None:
                print(temp.value, end=" ")
                temp=temp.next

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None
            
customQueue=Queue()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
customQueue.Display()
print()
print("Node is deleted: ",customQueue.deQueue())
print()
customQueue.Display()
print()
print("Peek Element is: ",customQueue.peek())

    