#1B
import random
n = int(input("Ingrese tamaño de lista: "))
lista = []

for i in range(n):
    lista = lista + [random.randint(10,99)]
print(lista)