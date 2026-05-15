input=[5,7,2,3,7,8,2,3,3]
target=3

count=0
for i in range(0, len(input)):
    if input[i]==target:
        count+=1
print(count)
