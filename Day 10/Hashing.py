# Hashing ----> Technique which is use to convert the data into the fix value 
# TC -----> O(1)  

#    What is Hash function ?
#--> Converts into fixed Index

# Properties of good hash function
# 1) Deterministic
# 2) fast Calculation
# 3) Unifrom Distribution

# ASCII values:
# C=67
# A=65
# T=84 

class HashTable:
    def __init__(self, size):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index=self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)
    
Obj=HashTable(5)
Obj.insert(10)
Obj.insert(20)
Obj.insert(30)
Obj.insert(40)
Obj.insert(50)
Obj.display()
print()
Obj.hash_function(10)
Obj.display()