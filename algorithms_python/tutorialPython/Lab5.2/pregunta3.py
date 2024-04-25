num = int(input("Ingrese tamaño de la lista: "))

array = []
for i in range(num):
    word = input(f'Tell me the {i + 1} word')
    array = array + [word]
print(array)