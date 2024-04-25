#1. ENCRIPTAR
def encripta(k,cad):
    #k es el desplazamiento
    if k > 0:
        s = ""
        for i in range(0, len(cad)):
            simb = cad[i]
            cod = ord(simb)
            if cod >= 65 and cod <= 90: #MAYUSCULA
                if cod + k <=90:
                    cod = cod + k
                else:
                    cod = 64 + (cod+k)%90
            else:
                if cod >= 97 and cod <= 122: #MINUSCULA
                    if cod + k <= 122:
                        cod = cod + k
                    else:
                        cod = 97 + (cod+k)%122
            s = s + chr(cod)
        print("Mensaje encriptado: ", s)
    else:
        s = ""
        for i in range(0, len(cad)):
            simb = cad[i]
            cod = ord(simb)
            if cod >= 65 and cod <= 90: #MAYUSCULA
                if cod + k >= 65:
                    cod = cod + k
                else:
                    cod = 91 - (65-(cod+k))
            else:
                if cod >= 97 and cod <= 122: #MINUSCULA
                    if cod + k >= 97:
                        cod = cod + k
                    else:
                        cod = 123-(97-(cod+k))
            s = s + chr(cod)
        print("Mensaje encriptado: ", s)
        return s

# 2. DESENCRIPTANDO
encriptacion = input("Ingrese el mensaje encriptado: ")
for i in range(-26,27):
    encripta(i,encriptacion)
