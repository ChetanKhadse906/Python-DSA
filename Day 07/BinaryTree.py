# BinaryTree 
# There are two ways to Implement BinaryTree
# 1. LinkedList
# 2. List (Array) 
class Tree:
    def __init__(self,data):
        self.data=data  #("Drinks")
        self.child=[]

    def __str__(self, level=0):
        ret=" "* level + str(self.data) + "\n"
        for ch in self.child:
            ret+=ch.__str__(level+1)
        return ret 

    def addChild(self, object):
        self.child.append(object)
        print("Tree Node is added")

rootNode=Tree("Drinks")
Hot     =Tree("Hot")
Cold    =Tree("Cold")
Tea     =Tree("Tea")
Coffee  =Tree("Coffee")
NonAlcoholic = Tree("Non Alcoholic")
Alcoholic    = Tree("Alcoholic")

rootNode.addChild(Hot)
rootNode.addChild(Cold)
Hot.addChild(Tea)
Hot.addChild(Coffee)
Cold.addChild(NonAlcoholic)
Cold.addChild(Alcoholic)

print(rootNode)