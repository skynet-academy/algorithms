msj = input("Ingrese frase: ")

def minus(msj):
    acum = ""
    for i in range(len(msj)):
        s = msj[i]
        if s >= "A" and s <= "Z":
            num = ord(s) + 32
            s = chr(num)
        elif s == "Ñ":
            s = "n"
        elif s == "Á":
            s = "á"
        elif s == "É":
            s = "é"
        elif s == "Í":
            s = "i"
        elif s == "Ó":
            s = "ó"
        elif s == "Ú":
            s = "ú"
        acum = acum + s
    return acum
print("La frase modificada: ", minus(msj))


