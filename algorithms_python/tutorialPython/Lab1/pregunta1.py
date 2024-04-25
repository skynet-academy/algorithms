import random
#contarode de Ws
cw = 0
#contador de las demás letras
c = 0

while cw < 20:
    c += 1
    i = chr(random.randint(ord("a"), ord("z")))
    if i == "w":
        cw += 1
    print(i, end=", ")
print("\nCantidad de Ws: ", cw,"\nCantidad del resto de letras: ", c)