# mylist=[44,22,77,0,9,88]
# for i in mylist:
#     print(i)

# mylist=[0,1,4,0,2,5]
# for i in mylist:
#     if i==0:
#         mylist.remove(i)
#         mylist.append(i)
# print(mylist)

# Find the second largest element
# list1=[7,3,9,2,8]
# list1.sort()

# print(list1[-2])

# a=[1,2,3,4,5,6,7,8,9,]
# a[::2]=10,20,30,40,50,60   # value
# print(a)


# a=[1,2,3,4,5]
# print(a[3:0:-1]) 

# arr=[[1,2,3,4],
#     [4,5,6,7],
#     [8,9,10,11],
#     [12,13,14,15]]

# for i in range(0,4):
#     print(arr[i].pop())

# fruit_list1=["Apple","Berry","Cherry","Papaya"]
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]="Gaurav"
# fruit_list3[1]="Kiwi"

# sum=0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0]=="Gaurav":
#         sum+=1
#     if ls[1]=="Kiwi":
#         sum+=20
# print(sum)

# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

mylist=[]
N=int(input("Enter the value of N: "))
for i in range(N):
    val=int(input("Enter the value: "))
    mylist.append(val)
print(mylist)

sum=0
for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum+=abs(mylist[i]-mylist[i+1])
print(sum)



