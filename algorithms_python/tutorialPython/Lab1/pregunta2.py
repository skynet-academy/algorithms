msj = input("Ingrese mensaje: ")
acum = ""
for i in range(len(msj)):
    if msj[i] >= "a" and msj[i] <= "z":
        acum = acum + chr(ord(msj[i])-32)
    else:
        acum = acum + msj[i]

aux = acum
acum = ""

for j in range(len(aux)):
    if aux[j] >= "A" and aux[j] <= "Z":
        if aux[j] == "Z":
            acum = acum + "A"
        else:
            acum = acum + chr(ord(aux[j])+1)
    else:
        if aux[j] >= "0" and aux[j] <= "9":
            if aux[j] == "0":
                acum = acum + "9"
            else:
                acum = acum + chr(ord(aux[j])-1)
print("Mensaje encriptado:", acum)