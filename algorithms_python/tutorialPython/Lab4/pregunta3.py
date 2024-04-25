msj = input("Ingrese un carácter : ")

def letra(msj):
    if len(msj) > 1:
        flag = False
    elif msj >= "a" and msj <= "z":
        flag = True
    elif msj >= "A" and msj <= "Z":
        flag = True
    elif msj == "á" or msj == "é" or msj == "í" or msj == "ó" or msj=="ú" or msj == "ü":
        flag = True
    elif msj == "Á" or msj == "É" or msj == "Í" or msj == "Ó" or msj == "Ú" or msj == "Ü":
        flag = True
    elif msj == "ñ" or msj == "Ñ":
        flag = True
    else:
        flag = False
    return flag
print("¿El carácter ingresado es letra?: ", letra(msj))
