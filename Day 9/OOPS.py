# class Student:
#     # By using class name we can access static method
#     @staticmethod  # decorator
#     def get_personal_detail(firstname, lastname):
#         print("Your Personal Detail= ", firstname, lastname)

#     @staticmethod
#     def contact_detail(mobile_no, roll_no):
#         print("Your Contact Detail=", mobile_no, roll_no)
    
# Student.get_personal_detail("Prashant Sir", 1001)
# Student.contact_detail(9923595773, 1001)

# 1) Inheritance ---------> Code Reusability
# Single level Inhritance
# class College: # parent class
#     def college_name(self):
#         print("Modern College")
    
# class Student(College):  # child class
#     def student_info(self):
#         print("Name: Prashant Jha Sir")
#         print("Branch: Mechanical")

# obj=Student()  # object create child class
# obj.college_name()
# obj.student_info()


# Multi level Inhritance
# class College: # parent class
#     def college_name(self):
#         print("Modern College")
    
# class Student(College):  # child class
#     def student_info(self):
#         print("Name: Prashant Jha Sir")
#         print("Branch: Mechanical")

# class Exams(Student):   # child class
#     def subject(self):
#         print("Subject1: Design Engineering")
#         print("Subject2: Math")
#         print("Subject3: C-Language")
# obj=Exams()
# obj.college_name()
# obj.student_info()
# obj.subject()

# Multiple Inheritance
# class SubMarks:
#     math=int(input("Enter paper of math: "))
#     DE=int(input("Enter paper marks of design Engineering: "))
#     C=int(input("Enter paper marks of C Language: "))
#     English=int(input("Enter paper marks of English: "))

# class PractMarks:
#     cpract=int(input("Enter practicals marks of C Language: "))

# class Result(SubMarks, PractMarks):

#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.C>=40 and self.English>=40  and self.cpract>=20:
#             print("Pass")
#         else:
#             print("Fail")
        
# obj=Result()
# obj.total()

# class add1:
#     def add(self,a,b):
#         print("add1")
#         return a+b
# class add2:
#     def add(self,a,b):
#         print("add2")
#         return a+b

# class D(add1,add2):
#     def method(self):
#         print("Main Class")
# Obj=D()
# print(Obj.add(10,20))
# print(Obj.add(20,30))
# Obj.method()


# 2) Polymorphism          -----> python only supports methdo over loading 
class RBI:
    def Home_loan(self):
        print("Home loan= 8%")

    def Education(self):
        print("Education loan= 9%")

class SBI(RBI):
    def Education_loan(self):
        print("Education loan= 10%")
        super().Education_loan()

Obj=SBI()
Obj.Education_loan()


# class RBI:
#     def __init__(self):
#         print("Parent Class Constructor")

# class SBI(RBI):
#     def __init__(self):
#         print("Child Class Constructor")
# Obj=SBI()





