# 1)
# import re
# count=0
# pattern=re.compile("function") # string converts ibnto bytecode
# # print(pattern)

# matcher=pattern.finditer("A function in python is defined by a def statement. The general syntax looks this: def function-name(Parameter list): statements, i.e. the function body. The parameter python list consists of none or more parameters. ")

# for i in matcher:  #i=0
#     count+=1
#     print(i.start(), "......",i.end(),"......",i.group())
# print("The number of occurences: ",count)

# 2)
# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")

# for i in matcher: # loop 4 times execute HiHiHiHi
#     count+=1
#     print(i.start(),"......",i.end(),"....",i.group())
# print("The number of occurrences: ",count)

# 3)
# import re
# obj=input("Enter any Character: ")  #7
# objmatch=re.finditer(obj,"a7bbb @k9z")
# #print(objmatch)
# for match in objmatch:
#     print(match.start(),".....",match.end(),".....",match.group())

# 4)
# import re
# a=input("Enter String to perform match operation: ")
# mtch=re.match(a, "Python is very Important Langauge")
# print(mtch)

# if mtch!=None:
#     print("match found at beginning level")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("There is no matching at beginning level")

# 5)
# import re 
# a=input("Enter String to perform match operation: ")       # If all match is found then it returns the object else it returns none
# mtch=re.fullmatch(a, "Python is very Important Langauge") 
# print(mtch)

# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("Full match not found")

# 6)
# import re
# s=input("Enter Email Id:")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
# if m!=None:
#     print("Valid E-Mail Id")
# else:
#     print("Invalid E-Mail Id")

#7) valid mobile number
# import re
# mo=input("Enter mobile number: ")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("Valid Mobile Number")
# else:
#     print("Invalid Mobile Number")

# 8)
# import re
# a=input("Enter String to performs match operation:  ")
# mtch=re.search(a, "Python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ", mtch.end(), " ", mtch.group())
# else:
#     print("There is no matching anywhere: ") 

# 9)
# import re
# mtch=re.findall("[a-z]","abch3hdh5bk7zQ$&")
# print(mtch)

# 10)
# import re
# obj=re.sub("[a-z]", "*", "2345 ABCD habc deff")
# print(obj)

# 11)
# import re
# obj=re.subn("[0-7]","@","ab3gd6nk17")
# print(obj)
# print("The String is: ", obj[0])
# print("The number of replacement is=", obj[1])

# 12)
# import re

# f1=open("File.txt", "r")
# f2=open("Output.txt", "w")

# text=f1.read()
# f2.write(text)

# print(f1)

# 13) Program to print the number of lines, words and characters present in the given files?
import os.sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists: ", fname)
    f=open(fname, "r")
else:
    print("File does not exist: ",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("The number of Lines: ",lcount)
print("The numbeer of Words: ",wcount)
print("The number of Characters: ",ccount)
