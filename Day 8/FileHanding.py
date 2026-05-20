# import csv
# f=open("employee.csv", 'a')
# a=csv.writer(f)
# # a.writerow(["EmpID", "Emp Name", "Emp Age"])

# empId=int(input("Enter your Empid: "))
# empName=input("Enter Employee Name: ")
# age=int(input("Enter Employee age: "))
# a.writerow([empId, empName, age])
# print("file has created")

import csv
f=open("student.csv", 'a')
a=csv.writer(f)
StudId=int(input("Enter Student Id: "))
StudName=input("Enter Student Name: ")
Phy=int(input("Enter Physics Marks: "))
Chem=int(input("Enter Chemistry Marks: "))
Mathematics=int(input("Enter Mathematics Marks: "))
Percentage=(Phy+Chem+Mathematics)/3
a.writerow([StudId, StudName, Phy, Chem, Mathematics, Percentage])
print("file has created")



