msj = input("Ingrese mensaje: ")
acum = ""
c1 = c2 = 0

for i in range(len(msj)):
    if msj[i] == " ":
        c2 += 1
        print(acum, c1)
        if c2 == 1:
            MAX = c1
            aux = acum
        else:
            if c1 > MAX:
                MAX = c1
                aux = acum
        acum = ""
        c1 = 0
    else:
        c1 += 1
        acum = acum + msj[i]
    if i == (len(msj)-1):
        print(acum, c1)
        if c1 > MAX:
            MAX = c1
            aux = acum
print("La palabra más larga es: ", aux)


