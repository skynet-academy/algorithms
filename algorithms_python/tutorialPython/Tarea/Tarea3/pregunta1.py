import random
#generar aleatoraiamente la longitud de la contraseña entre 2 y 15
n = random.randint(2,15)
#cremos la contraseña
contraseña = ""
for i in range(n+1):
    contraseña += chr(random.randint(32, 122))
print("Cadena generada: ",contraseña)

#Contamos la longitud de la cadena generada
lon_con = len(contraseña)
nivel = ""
#evaluamos un nivel de la contraseña
if lon_con <= 4:
    nivel = "malo"
elif lon_con <= 8:
    nivel = "regular"
else:
    nivel = "bueno"

# Contamos las minúsculas, mayúsculas y dígitos en el texto
minusculas = 0
mayusculas = 0
digitos = 0

for d in contraseña:
    ind = ord(d)
    if ind >= 97 and ind <= 122:
        minusculas += 1
    elif ind >= 65 and ind <= 90:
        mayusculas += 1
    elif ind >= 48 and ind <= 57:
        digitos +=1

#validamos la contraseña
if " " in contraseña:
    print("Contraseña correcta: ", False)
elif minusculas >= 1 and mayusculas >= 1 and digitos >= 1:
    print("Contraseña correcta: ",True)
    print("Nivel de seguridad: ",nivel)
else:
    print("Contraseña correcta: ", False)



