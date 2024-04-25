msj = input("Ingrese mensaje: ")
print("Tamaño del mensaje: ", len(msj))
acum = ""

for i in range(0, len(msj)):
    a = msj[i]
    if a != " ":
        acum = acum + a
        c = 0
    else:
        c += 1
        if c == 1:
            acum = acum + a
print("Frase modificada: ", acum)
