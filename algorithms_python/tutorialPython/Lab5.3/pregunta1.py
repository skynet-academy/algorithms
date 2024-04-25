def validar(pwd): #pwd es password
    if len(pwd) < 8:
        return False
    #si está formado solo por dígitos o solo por caracteres alfabetoicos da false
    if pwd.isdigit() or pwd.isalpha():
        return False
    if pwd.isalnum() == False:
        return False
    #debe contener al menos dos dígitos (números)
    Cont_dig = 0 #contador de dígitos
    for simb in pwd:
        if simb.isdigit():
            Cont_dig += 1
    return Cont_dig >= 2
#######
cad = input("Ingrese contraseña: ")
y = validar(cad)
if y == True:
    print("contraseña válida")
else:
    print("contraseña inválida")