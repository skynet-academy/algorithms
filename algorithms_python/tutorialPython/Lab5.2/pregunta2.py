from Funciones.funciones import *
n = int(input("Ingrese tamaño de lista: "))
x = genlista(n)
print(x)
z = []
z = z + [valor_min(x)] #z[0]: comienza en 0
for i in range(n-1):
    x = eliminar_min(x)
    print(x)
    z = z + [valor_min(x)]
    print(z)