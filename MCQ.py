# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

# WAP to accept student name and Marks from the keyword, and creates a dictionary. Also display student marks by taking student name 
n=int(input("Enter the number of students: "))
d={}
for i in range(n):
    name=input("Enter Student Name: ")
    marks=input("Enter Student Marks: ")
    d[name]=marks
while True:
    name=input("Enter Student Name to get Marks: ")
    marks=d.get(name, -1)
    if marks==-1:
        print("Student Not Found")
    else:
        print("The Marks of", name, " are", marks)
    option=input("Do you want to find another Student Marks[Yes/No]: ")
    if option=="No":
        break
print("Thanks for using our application")