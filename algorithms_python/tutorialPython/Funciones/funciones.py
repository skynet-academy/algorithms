import random

def genlista(n):
    lista = [None]*n
    for i in range(len(lista)):
        lista[i] = random.randint(-20,20)
    return lista

######

def suma(lista):
    s = 0
    for item in lista:
        s = s + item
    return s

######

def valor_max(lista):
    max = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

######

def valor_min(lista):
    min = lista[0]
    for i in range(0, len(lista)):
        if lista[i] < min:
            min = lista[i]
    return min

###############################

def eliminar_min(lista):
    flag = True
    y = []
    print(valor_min(lista))
    for i in range(len(lista)):
        if lista[i] == valor_min(lista) and flag:
            flag = False
        else:
            y = y + [lista[i]]
    return y

######

def verificar(p, zlista):
    flag = False
    for i in range(len(zlista)):
        if p == zlista[i]:
            flag = True
    return flag

######

def repetido(xlista):
    z = []
    for i in range(len(xlista)):
        if verificar(xlista[i],z) == False:
            z = z + [xlista[i]]
    return z

######

def palabra(n):
    a = []
    for i in range(n):
        d = input("Ingrese una palabra: ")
        a = a + [d]
    return a