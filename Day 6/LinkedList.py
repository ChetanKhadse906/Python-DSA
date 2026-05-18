# Types of variable (Instance variable)
# Instance variable depends on Object, whenever we create new objcet Instance variable will create an seperate memory for an object.abs
# static variable will only create one Memory

# class New:
#     def __init__(self):
#         self.a=10
# Obj1=New()
# Obj2=New()
# Obj3=New()
# Obj1.a=20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

# class New:
#     a=10

#     def __init__(self):
#         self.name="Prashant Sir"
# Obj1=New()
# Obj2=New()
# Obj3=New()
# New.a=50

# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)

class College:
    collegename="Modern College"  # static variable

    def __init__(self):
            self.studentname="Prashant"

principal=College()
teacher=College()
accountant=College()

print("principal= " ,principal.collegename, ".........", principal.studentname)
print("teacher= ", teacher.collegename, ".......", teacher.studentname)
print("accountant= ", accountant.collegename, ".........", accountant.studentname)
