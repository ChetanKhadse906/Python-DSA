class BSTNode:
    def __init__(self, data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

def insertNode(rootNode, nodeValue):# 70->50->90->30
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

            
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def InOrderTraversal(rootNode):
    if not rootNode:
        return
    InOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    InOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")


# search a node in Tree
def searchNode(rootNode, nodeValue):
    if rootNode.data==None:
        print("Tree has no nodes")
    elif rootNode.data==nodeValue:
        print("The value is found")
    elif nodeValue<=rootNode.data:
        if rootNode.leftChild.data==nodeValue:
            print("Value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else: # nodeValue>rootNode.data:
        if rootNode.rightChild.data==nodeValue:
            print("Value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

newBST=BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
insertNode(newBST, 10)
print("PreOrder Traversal: ")
preOrderTraversal(newBST)
print()
print("InOrder Traversal: ")
InOrderTraversal(newBST)
print()
print("PostOrder Traversal: ")
postOrderTraversal(newBST)

searchNode(newBST, 100)