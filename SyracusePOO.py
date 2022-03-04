import numpy as np

class Syracuse :
    def __init__(self,number1,number2):
        self.d=number1
        self.n=number2
        
    def calcul(self):
        
        print(self.d)

        i = 0

        while i < self.n :
            if self.d % 2 == 0:
                self.d = self.d // 2  
            else :
                self.d = self.d * 3 + 1
            i +=1

            print(self.d)


datatext=np.loadtxt(fname="data.txt")

       
print("CONJECTURE DE SYRACUSE POO")
print("Contenu du txt :",datatext)

d=int(datatext[0])
n=int(datatext[1])

test=Syracuse(d,n)
test.calcul()