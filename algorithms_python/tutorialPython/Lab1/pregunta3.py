msj = input("Ingrese el mensaje: ")

for i in range(ord("A"), ord("z")+1):
    c = 0
    for j in range(len(msj)):
        if chr(i) == msj[j]:
            c += 1
    if c > 0:
        print(chr(i) +":",c, end=", ")