# Find the key with the Maximum Value in a Dictionary
# dict={"A":50, "B":30,"C":70}
# for i in dict



# Find the key with the Minimum Value in a Dictionary
# input={"X":20,"Y":10,"Z":30}

# 7) Count Frequency of Elements in a List using a Dictionary
# input=[1,2,2,3,4,3,5]
# dict={}
# for i in input:
#     dict[i]=input.count(i)
# print(dict)


# 123456=654321
# num=123456
# print("Original: ", num)
# a=num%10
# num//=10
# b=num%10
# num//=10
# c=num%10
# num//=10
# d=num%10
# num//=10
# e=num%10
# num//=10
# f=num%10
# num//=10
# rev=a*100000+b*10000+c*1000+d*100+e*10+f*1
# print("Reverse: ", rev)

Amount=int(input("Please Enter Amount for Withdraw: "))
print(" 100 notes= ", Amount//100)
print(" 50 notes= ", (Amount%100)//50)
print(" 20 notes= ",((Amount%100)%50)//20)
print(" 10 notes=", (((Amount%100)%50)%20)//10)
print(" 5 notes= ", ((((Amount%100)%50)%20)%10)//5)
print(" 2 notes")







