import random
n = int(input("Ingrese tamaño de lista: "))
lista = [None]*n
s = 0

for i in range(len(lista)):
    lista[i] = random.randint(10,99)
    s = s + lista[i]
print(lista)
prom = s/len(lista)
print(prom)

c = 0
for j in range(len(lista)):
    if lista[j] > prom:
        c += 1
print("Número de elementos mayores que el prom: ", c)