# for i in range(5): #i=0 by default
#     print(i)

# for(Initialisation: Condition: Updation)
# for i in range(2,11,2):  
#     print(i)

# for i in range(5,0,-1):  # -1 for decrement by 1 value
#     print(i)

# # Printing 2 table
# for i in range(1,11): # id
#     print(i*2, " ", i*3, " ", i*4," ", i*5," ",i*6," ",i*7," ",i*8," ",i*9," ",i*10," ")
# print(" ")

# print("------------------------------------------------------------------------------------------")

# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13," ",i*14," ",i*15," ",i*16," ",i*17," ",i*18," ",i*19," ",i*20)

# WAP to accept 3 paper marks and calculate total, percentage and check if he/she pass in all, the subjects 
# if per>65 --> and gender="male" -----> eligible for Placementss else not eligible

# sub1=int(input("Enter the subject1 marks: "))
# sub2=int(input("Enter the subject2 marks: "))
# sub3=int(input("Enter thw subject3 marks:  "))
# Total=sub1+sub2+sub3
# Percentage=Total/3.0
# print("Total=", Total)
# print("Percentage=", Percentage)
# if sub1>=40 and sub2>=40 and sub3>=40:
#     print("Pass")
# else:
#     print("Fail")    
# gender=input("Enter your gender M/F: ")
# if Percentage>=65 and gender=="M":
#     print("You are elligible for the Placement")
# else:
#     print("You are not eligible for the Placement")

# for i in range(1,6):
#     if i==3:
#         continue
#     print(i, " " , 6-i)

# using zip function
for i,j in zip(range(1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i, " ", j)



