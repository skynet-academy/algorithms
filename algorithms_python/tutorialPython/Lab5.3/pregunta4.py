cad = "hola como estas"
a = cad.title()
print(a)

cad2 = "el enanito estuvo por aqui"
b = cad2.replace("e", "E")
print(b)

c = b.startswith("Hola") and b.endswith("saludos")
print("Incio con la palabra ¨Saludos¨ y termina con ¨saludos¨?", c)

#cad = "Inicia con la palabra"
d = b.capitalize()
print(d)

e = d.swapcase()
print(e)

e = "  i love python   "
f = e.strip(" ") #para quitar los espacioes sobrantes
print(f)

g = f.replace(" ", "")
print(g)

g = "hola   buenas   tardes"
lst = g.split()
h = " ".join(lst)
print(h)
