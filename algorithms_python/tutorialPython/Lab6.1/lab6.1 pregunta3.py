#Inciso a
def sumar_lista(lista):
    acum = 0
    for item in lista:
        acum += item
    return acum

numeros = [7, 2, 22]

print(sumar_lista(numeros))

#Inciso b
matriz_colum = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def sumar_colum(colum):
    suma_colum = []
    for i in range(len(matriz_colum[0])):
        acum_colum = 0
        for j in range(len(matriz_colum)):
            acum_colum += matriz_colum[j][i]
        suma_colum.append(acum_colum)
    return suma_colum
print(sumar_colum(matriz_colum))

#Inciso c
matriz_fila = [
    [70, 20, 22],
    [55, 37, 11],
    [17, 19, 57]
]

def sumar_fila(fila):
    suma_fila = []
    for k in range(len(matriz_fila)):
        acum_fila = 0
        for l in range(len(matriz_fila[0])):
            acum_fila += matriz_fila[k][l]
        suma_fila.append(acum_fila)
    return suma_fila
print(sumar_fila((matriz_fila)))