# name="prashant*is*a*good*programmer"   # output = ****prashantisagoodprogrammer
# newname=" "
# val=""

# for i in name:
#     if i!='*':
#         newname+=i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))

# name="aaabbbbccceeeee"
# newname={}
# for i in range(len(name)):
#     key=name[i]
#     count=0
#     for j in range(len(name)):
#         if key==name[j]:
#             count+=1
#     newname[key]=count
# # print(newname)
# for i,j in newname.items():
#     print(i,j,sep='',end='')
    

salary=int(input("Enter your salary: "))
rating=int(input("Enter your preference appraisal rating: " ))
increment=0
if rating>=1 and rating<=3:
    increment=salary*10/100
elif rating>=3.1 and rating<=4:
    increment=salary*30/100
elif rating>=4.1 and rating<=5:
    increment=salary*40/100
else:
    print("Invalid rating")
print("Incremented Salary: ", increment+salary)


