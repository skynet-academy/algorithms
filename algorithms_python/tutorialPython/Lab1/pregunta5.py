msj1 = input("Ingrese primera palabra: ")
msj2 = input("Ingrese segunda palabra: ")
acum = 0

if len(msj1) < len(msj2):
    for i in range(len(msj1)):
        print(msj1[i], msj2[i])
    for j in range(len(msj2)-len(msj1)):
        print(" ", msj2[len(msj1)+j])
else:
    for i in range(len(msj2)):
        print(msj1[i], msj2[i])
    for j in range(len(msj1)-len(msj2)):
        print(msj1[len(msj2)+j]," ")