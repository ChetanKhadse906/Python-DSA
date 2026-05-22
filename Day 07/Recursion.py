# Recursion -------> when the main problem can be divided into similar sub problem 
#                     like in Tree we have proform BFS, DFS Preorder, Inorder 
# Recursion use Stack Memory so avoid using Recursion 

# 1) Factorial
# def factorial(num):
#     if num<=1:  # base condition
#         return 1
#     return num * factorial(num-1)

# print(factorial(4))

# 2) CapitalizeFirst Solution Using Recursion 
# def capitalizeFirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
    
#     result.append(arr[0][0].upper() + arr[0][1:])  # T+aco = Taco
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car', 'taco', 'banana']))      #['Cars', 'Taco', 'Banana']

# 3) power
# def power(base, exponent):
#     if exponent==0:
#         return 1

#     return base * power(base, exponent-1)

# print(power(2,0))   # 1
# print(power(2,2))   # 4
# print(power(2,4))   # 16

# 4) Product of Array
# def productOfArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))        #6
# print(productOfArray([1,2,3,10]))     #60

# 5) Reverse String 
# def reverse(string):
#     if len(string)<=1:
#         return string   
#     return string[len(string)-1] + reverse(string[0:len(string)-1])

# print(reverse('python'))
# print(reverse('appmillers'))

# 6) recursiveRange
# def recursiveRange(num):
#     if num<=0:
#         return 0
#     return num + recursiveRange(num-1)

# print(recursiveRange(6)) 

# 7) Reverse String
# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])

# print(isPalindrome('awesome'))
# print(isPalindrome('malayalam'))

# 8) someRecursive Solution
def someRecursive(arr, cb):
    if len(arr)==0:
        return False
    if not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

def  isOdd(num):
    if num%2==0:
        return False
    else:
        return True

print(someRecursive([1,2,3,4], isOdd))
print(someRecursive([4,6,8,9], isOdd))
print(someRecursive([4,6,8], isOdd))



