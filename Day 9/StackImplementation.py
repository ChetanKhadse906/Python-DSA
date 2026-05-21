# Stack Implementation Using Linekd List
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class LinkedList:   
    def __init__(self):
        self.head=None

    def __iter__(self):
        curNode=self.head
        while curNode:
            yield curNode            # yield ------> keyword is used to return the value yeild keyword is a part of generator, when their is large amount of data so to return the data fast we use yeild keyword to return the data fast which is a part of generator
            curNode=curNode.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()

        
    def isEmpty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    
    def push(self, value):
        node=Node(value)
        node.next=self.LinkedList.head
        self.LinkedList.head=node
        print("Element is Pushed")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            nodeValue=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next

            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            nodeValue=self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head=None
    
    def Display(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            temp=self.LinkedList.head

            while temp != None:
                print(temp.value)
                temp=temp.next

    # def __str__(self):
    #     values=[str(x.values) for x in self.LinkedList]
    #     return '\n'.join(values)

customStack=Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.Display()
print()
print("Peek Element is: ", customStack.peek())
print("Element is Popped: ",customStack.pop())
