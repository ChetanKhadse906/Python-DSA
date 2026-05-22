# # 1) Insertion Sort 
# arr=[3,5,8,6,2]
# def InsertionSort(arr):
#     for i in range(1, len(arr)):
#             key=arr[i]
#             j=i-1

#             while j>=0 and arr[j]>key:
#                 arr[j+1]=arr[j]
#                 j=j-1
#             arr[j+1]=key
#             print(arr)
        
# InsertionSort(arr)
# print(arr)

# 2) Selection Sort 
arr=[20,12,10,15,2]

def SelectionSort(arr):
    for i in range(0, len(arr)):
        min=i
        j=i+1

        while j<len(arr):
            if arr[j]<arr[min]:
                min=j
            j=j+1

        arr[i],arr[min]=arr[min],arr[i]
           print(arr)
    
SelectionSort(arr)
print(arr)
