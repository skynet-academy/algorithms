msj = input("Ingrese una frase: ")
def mod(msj):
    acum = ""
    for i in range(len(msj)):
        carac = msj[i]
        if carac == "ñ":
            acum = acum + "n"
        elif carac == "á":
            acum = acum + "a"
        elif carac == "é":
            acum = acum + "e"
        elif carac == "í":
            acum = acum + "i"
        elif carac == "ó":
            acum = acum + "o"
        elif carac == "ú" or carac == "ü":
            acum = acum + "u"
        else:
            acum = acum + carac
    return acum
print("La frase modificada: ", mod(msj))