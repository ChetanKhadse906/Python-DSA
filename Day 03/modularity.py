# modularity approach in function
import sys
def add():
    a=int(input("Enter value of A: "))
    b=int(input("Enter value of B: "))
    print(a+b)

def sub():
    a=int(input("Enter value of A: "))
    b=int(input("Enter value of B: "))
    print(a-b)

def div():
    a=int(input("Enter value of A: "))
    b=int(input("Enter value of B: "))
    print(a/b)

def mul():
    a=int(input("Enter value of A: "))
    b=int(input("Enter value of B: "))
    print(a*b)

while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        add() # calling function
    elif choice==2:
        sub()  # calling funcction
    elif choice==3:
        div() # calling function
    elif choice==4:
        mul() # calling function
    elif choice==5:
        sys.exit()


