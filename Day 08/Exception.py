# 1) Exception
# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     print(a/b)

# # except ZeroDivisionError:
# #     print("Can't divide by zero") 
# # except ValueError:
# #     print("Enter only Integer value")
# # except:
# #     print("ABC")

# except (ZeroDivisionError, ValueError) as msg:
#     print(msg)

# 2) log
import logging
logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except (ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("Logging Level is ste up. Check 'newFile.txt' for log details.")


