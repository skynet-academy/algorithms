#Inciso a
def Ordenar_léxico(cad):
    lst = cad.split()
    lst.sort()
    nueva = " ".join(lst)
    return nueva

#Inciso b
def Ordenar_tamaño(cad):
    lst = cad.split()
    lst.sort(key=len)
    nueva = " ".join(lst)
    return nueva

#Inciso c
def Eliminar_duplicados(lst):
    nueva = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                #verificamos que en esté en la nueva lista para pasar a incluirla
                pasar = True

        for k in range(len(nueva)):
            if lst[i] == nueva[k]:
                pasar = False
            if pasar == True:
                nueva = nueva + [lst[i]]
    return nueva
#########
cad = "vamos a cambiar la oración"
print("N1. Ordenación lexicográfica")
y = Ordenar_léxico(cad)
print(y)
print("N2. Ordenar por tamanño")
z = Ordenar_tamaño(cad)
print(z)
cad = "el 3 de julio de 2008 salió"
lista = cad.split()
lst = Eliminar_duplicados(lista)
cadf = " ".join(lst)
print(cadf)