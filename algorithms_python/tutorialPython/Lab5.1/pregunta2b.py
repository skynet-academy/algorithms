import random
n = int(input("Ingerse tamaño de lista: "))
lista = []
s = 0

for i in range(n):
    lista = lista + [random.randint(10,99)]
    s = s + lista[i]
print(lista)
prom = s/n
print(prom)
c = 0

for item in lista:
    if item > prom:
        c += 1
print(c)