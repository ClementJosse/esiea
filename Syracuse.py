#Clément Josse

print("CONJECTURE DE SYRACUSE")

d=int(input("Nombre de départ :  "))
n=int(input("Nombre d'iterrations : "))

print(d)

i = 0

while i < n :
    if d % 2 == 0:
      d = d // 2  
    else :
        d = d * 3 + 1
    i +=1

    print(d)
