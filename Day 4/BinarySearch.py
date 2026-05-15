# def BinarySearch(array, target):
#     low=0
#     high=len(array)-1

#     while low<=high:
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79]
# target=72
# answer=BinarySearch(array, target)
# if answer==-1:
#     print("Element", target ," not found ")
# else:
#     print("Element", target ," found at index ", answer)

# # Bubble sort
# def BubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j]>array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp
#             print(array)
#         print()

# array=[64,34,25,12,22,11,90]
# BubbleSort(array)

# Security Key Problem
mylist=[5,7,8,3,7,8,9,2,3,4,4,4,4,4]
newlist=[]

for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=i+1

    while j<len(mylist):
        if key==mylist[j]:
            newlist.append(key)
        j=j+1
print(len(newlist))



