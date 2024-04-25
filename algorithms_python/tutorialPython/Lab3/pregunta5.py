from pregunta3 import *
x = int(input("Ingrese valor de x: "))
n = int(input("Ingrese canditad de términos: "))
c = -1
signo = 1
suma = 0

for i in range(n):
    c +=2
    pt = potencia(x,c)
    ft = factorial(c)
    suma = suma + signo*pt/ft
    signo = signo*-1
print("Suma: ", suma)