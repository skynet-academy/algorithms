
def reversa(msj):
    acum = ""
    for i in range(0, len(msj)):
        carac = msj[i]
        acum = carac + acum
    return acum
###
msj = input("Ingrese mensaje: ")
print("Texto invertido: ", reversa(msj))