
H = [ [3, 2, 1, 4, 5, 3, 3],
      [4, 5, 2, 3, 2, 4, 1],
      [2, 3, 2, 4, 1, 4, 5],
      [1, 4, 5, 3, 3, 3, 2],
      [3, 2, 1, 3, 2, 4, 1],
      [4, 5, 2, 4, 5, 3, 3]
      ]
print(H)

C = ["C", "A", "B", "B", "C", "A"]
P = [["A", 100],
     ["B", 80],
     ["C", 50]
     ]
print(" "*7, end="")
s = ""
for i in range(1,8):
    s = s + "Día "+ str(i) + " "
print(s)

c = 1
for fila in H:
    print("Obrero "+ str(c), end="")
    for item in fila:
        print("%5d"%item, end=" ")
    print()
    c = c + 1

print("a- Cuanto cobrará cada obrero por horas extras en la semana")
total_hora = []
for fila in H:
    total_hora.append(sum(fila))
print(total_hora)

#lista de tasas por cada obrero
precio = []
for item in C:
    for i in range(len(P)):
        if P[i][0] == item:
            precio.append(P[i][1])
print(precio)

mas_extras = []
for i in range(len(total_hora)):
    mas_extras.append(total_hora[i] * precio[i])
    print("Orero " + str(i+1) + ": " + str(mas_extras[i]))

print("b- Total pagado por dichas horas de la empresa: ", sum(mas_extras))

print("c- El obrero con mas horas extras")
print("Obrero", total_hora.index(max(total_hora)) + 1)

print("d- La categoria de obreros con mas horas extras: ", C[total_hora.index(max(total_hora))])
