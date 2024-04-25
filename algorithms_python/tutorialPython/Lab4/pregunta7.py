from pregunta6 import reversa
msj = input("Ingrese mensaje: ")
def palíndromo(msj):
    if msj == reversa(msj):
        flag = True
    else:
        flag = False
    return flag
if palíndromo(msj) == True:
    print("Es palíndromo")
else:
    print("No es palíndromo")