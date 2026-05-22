# Stack Implementation 
# Two ways
# 1) List/ Array     ----> for small amount of data
# 2) Linked List     ----> for large amount of data
# class ---> way to bind the data memeber and member function 
# data memeber --> variables, representa the property of the class
# method ----> declare inside the class 

# class Name:
#     age=30 
#     def display(self):     #self     ------> works like this keyword, to access the current properties of the class
#         print("Hello World")

# obj=Name()
# print(obj.age)
# obj.display()

# class Student:
#     def __inti__(self):
#         self.name="prashant"
#         self.age=30

#     def display(self):
#         print("Name=", self.name)
#         print("Age=",self.age)
# studObj=Student()
# print(studObj)

# 2)
# class Message:
#     def __init__(self):
#         print("I am Constructor")

#     def shows(self):
#         print("Class Program")
# obj=Message()                       # for one object consrtructor is called only one time (once)
# obj.shows()
# obj2=Message()

# 3) Parameterized Constructor
class StudentInfo:
    def __init__(self, name, age, roll_no):
        self.Name=name
        self.Age=age
        self.RollNo=roll_no

    def displayStudentInfo(self):
        print("Name=", self.Name)
        print("Age=", self.age)
        print("")

studentObj=StudentInfo("Prakash", 34,101)
studentObj.displayStudentInfo()
