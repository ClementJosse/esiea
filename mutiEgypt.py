#Clément Josse

print("MULTIPLICATION EGYPTIENNE")

a = int(input("Premier nombre : "))
b = int(input("Deuxième nombre : "))

i = 0

while a != 0 :
    if (a % 2) == 1 :
        i = i + b
    b = b + b
    a = a // 2

print(i)
