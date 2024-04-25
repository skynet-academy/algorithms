from funciones import *

#def verificar(p, zlista):
    #flag = False
    #for i in range(len(zlista)):
     #   if p == zlista[i]:
      #      flag = True
    #return flag

#def repetido(xlista):
 #   z = []
  #  for i in range(len(xlista)):
   #     if verificar(xlista[i],z) == False:
    #        z = z + [xlista[i]]
    #return z

n = int(input("Ingrese tamaño de lista: "))
y = genlista(n)
print(y)
l = repetido(y)
print(l)