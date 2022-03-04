#Clément Josse
import numpy as np

class Syracuse :
    def __init__(self,txt):
        self.d=int(txt[0])
        self.n=int(txt[1])
        
    def calcul(self):
        f=open("output.txt","w")
        f.write(str(self.d)+'\n')
        print(self.d)


        i = 0

        while i < self.n :
            if self.d % 2 == 0:
                self.d = self.d // 2  
            else :
                self.d = self.d * 3 + 1
            i +=1
            f.write(str(self.d)+'\n')
            print(self.d)

        f.close()


inputText=np.loadtxt(fname="input.txt")

       
print("CONJECTURE DE SYRACUSE POO")
print("Contenu du txt :",inputText)

test=Syracuse(inputText)
test.calcul()