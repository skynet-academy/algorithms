from funciones import *
def una_vez(x):
    z = []
    for i in range(len(x)):
        flag = False
        for j in range(len(x)):
            if j != i:
                if x[i] == x[j]:
                    flag = True
        if flag == False:
            z = z + [x[i]]
    return z

n = int(input("Ingrese tamaño de lista: "))
y = genlista(n)
print(y)
l = una_vez(y)
print(l)
