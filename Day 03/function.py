# # function     
# def hello():        # called function
#     print("Hello World")

# hello()  # calling function
# hello()

#
# def arithmetic():
#     a=int(input("Enter value of a: "))
#     b=int(input("Enter value of b: "))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub, div, mul   # retuns in the form of tuple*  In python it is possible to return multiple values

# # print(arithmetic())
# result=arithmetic()
# print("Arithmetic=", result)


# 3) How many types of argument we pass in function?
# 1. Positional arugument
# 2. Keyword argument
# 3. Default argument
# 4. Variable length argument / variable number of arguments

# 1. Positional argument
# def arithmetic(a, b):

#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub, div, mul   

# positional argument
# result=arithmetic(5, 5)
# print("Arithmetic=", result)


# 2. Keyword argument   here position doesn,t matter
# def credential(username, password):
#     if username==password:
#         print("login Successfully")

#     else:
#         print("Invalid Credentials")

# credential(username="admin", password="admin") # 3 calling function   keyword name and parameter name must be same 

# 3. default argument
# def cityName(city="Pune"): # default argument="Pune"
#     print(city)

# cityName("Nagpur")
# cityName("Mumbai")
# cityName()             # when we are passing any argument the default argument will be consider

# 4. variable length argument    number of argument at the same time 
def cityName(*name):          # * as a prefix parameter must accept all the agument in the tuple format
    print(name)

cityName("Nagpur", "Delhi", "Mumbai", "Pune")









