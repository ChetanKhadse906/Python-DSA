# def linearsearch(array, target):
#     for i in range(0, len(array)):
#         if array[i]==target:
#             return i
#     return -1

# array=[1,2,3,4,8,7,9]
# target=7
# ans=linearsearch(array, target)
# if ans==-1:
#     print("Target element not found")
# else:
#     print(target," found at index ", ans)

# Remove spaces from the String:
# 1) rstrip() --> To remove spaces at right side 
# 2) lstrip() --> To remove spaces at left side 
# 3) strip() --> To remove spaces both side 
city=input("Enter your city Name: ")
scity=city.strip()
if scity=='Hyderabad':
    print("Hello Hyderabadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi.Vanakkam")
elif scity=="Banglore":
    print("Hello Kannadiga..Shubhodaya")
else:
    print("your entered city is invalid")