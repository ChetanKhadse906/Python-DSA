# Tower of Hanoi
import  time
class Tower:
    def __init__(self): #Constructor
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem         A=[3,2,1]           B=[]         C[]")
        print()
        print("Expected Output       A=[]                B=[]            C[3,2,1]")
        self.A=[]
        self.B=[]
        self.C=[]

    def Tower(self, item):
        self.A.append(item)
        time.sleep(5)
        print("A=", self.A)
        print("Items in Tower A\n")

    def Pass1(self):
        self.temp=self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A      ,"    ", "B=", self.B     , "     ", "C=", self.C)
        print("Pass One Completed=====================\n")
    
    def Pass2(self):
        self.temp=self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Two Completed=======================\n")

      
    def Pass3(self):
        self.temp=self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Three Completed=======================\n")

    def Pass4(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Three Completed=======================\n")

    def Pass4(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Four Completed=======================\n")

    def Pass5(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Five Completed=======================\n")

    def Pass6(self):
        self.temp=self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Six Completed=======================\n")

    def Pass7(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(5)
        print("A=", self.A         , "     ",     "B=", self.B      ,"       ","C=", self.C)
        print("Pass Seven Completed=======================\n")

obj=Tower()
obj.Tower(3)
obj.Tower(2)
obj.Tower(1)
obj.Pass1()
obj.Pass2()
obj.Pass3()
obj.Pass4()
obj.Pass5()
obj.Pass6()
obj.Pass7()

    



    