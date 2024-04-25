from funciones import *
def contrario(lista):
    aux = []
    for element in lista:
        aux = [element] + aux
    return aux

def alfabéticas(lista):
    aux = []
    for i in range(1, len(lista)-1):
        if lista[i-1] < lista[i] and lista[i] < lista[i+1]:
            aux = aux + [lista[i]]
    return aux
######
#def palabra(n):
 #   a = []
  #  for i in range(n):
   #     d = input("Ingrese una palabra: ")
    #    a = a + [d]
    #return a
n = int(input("Ingrese tamaño de lista: "))
l = palabra(n)
print("Lista inicial es: ", l)
print("Inciso a")
l2 = contrario(l)
print("Lista en orden contrario: ", l2)
print("Inciso b")
l3 = alfabéticas(l)
print("Aquellas palabras mayores a la anterior \
        y menores a la posterior alfabeticamente: ", l3)