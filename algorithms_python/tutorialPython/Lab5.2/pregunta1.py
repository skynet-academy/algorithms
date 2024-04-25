from funciones import *
#def eliminar_min(lista):
 #   flag = True
  #  y = []
   # print(valor_min(lista))
    #for i in range(len(lista)):
     #   if lista[i] == valor_min(lista) and flag:
      #      flag = False
       # else:
        #    y = y + [lista[i]]
    #return y
n = int(input("Ingrese tamaño de lista: "))
l = genlista(n)
print(l)
z = eliminar_min(l)
print(z)