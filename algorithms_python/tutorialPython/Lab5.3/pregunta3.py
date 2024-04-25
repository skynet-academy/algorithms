def transformar(frase):
    lista = frase.split(",")
    lista.sort()
    nueva = "-".join(lista)
    return nueva
#######
cad = input("Ingrese una frase (para separar por comas): ")
print("Cadena trasnformada: ", transformar(cad))