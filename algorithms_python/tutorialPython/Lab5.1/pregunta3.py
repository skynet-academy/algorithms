from funciones import *
n = int(input("Ingrese tamaño de lista: "))
l = genlista(n)
print(l)
print("Suma de los valores: ", suma(l))
print("Valor máx: ", valor_max(l))
print("Valor mín: ", valor_min(l))