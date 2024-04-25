from pregunta3 import letra
from pregunta4 import digito
msj = input("Ingrese el mensaje: ")
def quitar(msj):
    acum = ""
    for i in range(len(msj)):
        carac = msj[i]
        if letra(carac) == True:
            acum = acum + carac
        elif digito(carac) == True:
            acum = acum + carac
    return acum
print("Frase modificada: ", quitar(msj))