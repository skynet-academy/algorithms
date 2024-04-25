import random

def genlista(n):
    lista = [None]*n
    for i in range(len(lista)):
        lista[i] = random.randint(-20,20)
    return lista

meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]

agencias = ["Agencia1", "Habich", "Agencia3", "Agencia4", "Agencia5"]

#obtener las ventas mesuales por agencia

A = []
for j in range(5):
    lst = genlista(12)
    A.append(lst)
print("a- Mostrar los datos en forma de una tabla")
print(" "*9, end="")
for i in range(len(meses)):
    print(meses[i], end=" ")
print()

#Mostrar las agenicas y sus ventas mensuales
for f in range(5):
    print(agencias[f], end=" ")
    for c in range(12):
        print("%3d"%A[f][c], end="")
    print()
print("b- Total de ventas en el año de la agencia Hbaich")
print(sum(A[1]))

print("c- Promedio de ventas el mes de diciembre")
suma = 0
for f in range(5):
    suma = suma + A[f][11]
prom = suma/5
print(prom)

print("d- Agencia que tuvo masyores ventas en mayo")
mayor_venta = A[0][4]
num_agen = agencias[0]
for f in range(1,5):
    if A[f][4] > mayor_venta:
        mayor_venta = A[f][4]
        num_agen = agencias[f]
print("Mayor venta: ", mayor_venta, "en", num_agen)

print("e- Mes con menores ventas del año")
valor_mes = []
for c in range(12):
    suma = 0
    for f in range(5):
        suma = suma + A[f][c]
    valor_mes = valor_mes + [suma]
print(valor_mes)

#mes con menor venta

mes_menor = min(valor_mes)
print("Mes:",meses[valor_mes.index(mes_menor)])