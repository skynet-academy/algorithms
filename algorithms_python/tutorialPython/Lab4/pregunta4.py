carac = input("Ingrese un caracter: ")

def digito(dig):
    if len(dig) > 1:
        flag = False
    elif dig >= "0" and dig <= "9":
        flag = True
    else:
        flag = False
    return flag
print("¿El carácter es un dígito?:", digito(carac))