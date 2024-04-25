from funciones import *
num = int(input("Ingrese tamaño de la lista: "))
l = genlista(num)
print(l)
print(suma(l))

for i in range(len(l)):
    if suma(l) > 0:
        if i%2 == 0:
            l[i] = 0
    else:
        if i%2 != 0:
            l[i] = 0
print(l)
