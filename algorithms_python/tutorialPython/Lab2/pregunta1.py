msj = input("Ingrese mensaje: ")
msj = " " + msj
acum = ""

for i in range(-1, -len(msj)-1, -1):
    a = msj[i]
    if a != " ":
        acum = a + acum
    else:
        print(acum)
        acum=""