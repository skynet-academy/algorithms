#1A
import random
n = int(input("Ingrese tamaño de lista: "))
lista = [None]*n

for i in range(len(lista)):
    lista[i] = random.randint(10,99)
print(lista)


