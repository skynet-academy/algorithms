msj1 = input("Ingrese la primera frase: ")
msj2 = input("Ingrese la segunda frase: ")
suma = ""
comun = ""
for i in range(ord("a"), ord("z")+1):
    suma = suma + chr(i)

for i in range(len(msj1)):
    a = msj1[i]
    for j in range(len(msj2)):
        if a == msj2[j]:
            flag = False
            for k in range(len(comun)):
                if a == comun[k]:
                    flag = True
            if flag == False:
                comun = comun + a
orden = ""

for i in range(len(suma)):
    letra = suma[i]
    for j in range(len(comun)):
        if letra == comun[j]:
            orden = orden + letra
if len(orden) > 0:
    print("Las letras en comunes son: ", orden)
else:
    print("No tienen letras en comun")

