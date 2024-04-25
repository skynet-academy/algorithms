from funciones import *
num = int(input("Ingrese tamaño de lista: "))
l = genlista(num)
print(l)
print(valor_max(l))
print(valor_min(l))

#Inciso a
lista1 = []
for i in range(num):
    if l[i] != valor_max(l) and l[i] != valor_min(l):
        lista1 = lista1 + [l[i]]
print(lista1)

#Inciso b
prom = suma(lista1)/len(lista1)
nega = []
posi = []

for j in range(len(lista1)):
    if lista1[j] < 0:
        nega = nega + [lista1[j]]
    else:
        posi = posi + [lista1[j]]
print(posi)
print(nega)