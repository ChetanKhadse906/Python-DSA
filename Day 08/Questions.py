# 1) 
# Input=[0,0,1,2,0,3,0,0,4]
# Output=[]
# print(Input)

# for i in range(0, len(Input)):
#     if Input[i]==0:
#         continue
#     else:
#         append(Output.)
# print(Output)

# 2) Find the first Missing Positive Integer
Input=[0,1,2,3,4,6,7,8,9,10]
print(Input)

max=Input[0]
for i in range(1, len(Input)):
    if Input[i]> max:
        max=Input[i]
print(max)

i=1
while i<=max:
    if i not in Input:
        print(i)
        break
    else:
        i=i+1
    