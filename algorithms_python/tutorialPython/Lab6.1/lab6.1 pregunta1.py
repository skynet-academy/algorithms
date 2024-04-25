#INCISO A
#número de filas
n = int(input("Ingrese n filas: "))
#número de columnas
m = int(input("Ingrese m columnas: "))

l = [None]*n
for f in range(n):
    l[f] = [None]*m
print(l)

#no hacer
#l = [[None]*n]m
#[None][None][None]

for f in range(n):
    for c in range(m):
        x = int(input("Ingrese un número: "))
        l[f][c] = x
print(l)

#INCISO B
#número de filas
p = int(input("Ingrese p filas"))
#número de columnas
q = int(input("Ingrese q columnas"))

#sin separar memorioa previamente
r = []

for i in range(p):
    r.append([])
    for j in range(q):
        y = int(input("Ingrese un número"))
        r[i].append(y)
print(r)
