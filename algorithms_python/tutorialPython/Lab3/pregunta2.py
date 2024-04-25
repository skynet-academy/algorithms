def left(m):
    i = 0
    acum = ""
    while m[i] == " ":
        i = i + 1
    for j in range(i, len(m)):
        acum = acum + m[j]

def right(m2):
    j = len(m2) - 1
    acum = ""
    while m2[j] == " ":
        j = j - 1
    for p in range(j+1):
        acum = acum + m2[p]
    return acum

def count(m3):
    q = 0
    for a in range(len(m3)):
        if m3[a] == " ":
            q = q + 1
    return q + 1

def clean():
    men = input("Texto: ")
    #limpiar al inicio
    men = left(men)
    print(men)
    #limpiar al final
    men = right(men)
    print(men)
    acum = ""
    e = 0
    for k in range(len(men)):
        if men[k] != " ":
            acum = acum + men[k]
            e += 1
        else:
            if e > 0:
                acum = acum + " "
            e = 0
    print(acum)
    x = count(acum)
    print("La cantidad de palabras es: ", x)

######
clean()


