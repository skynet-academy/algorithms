print("Bienvenido al mundo de los númeors primos")
print("Indique la opcion que desea realizar:")
print("\n1. Determinar si un número es primo \n2. Mostrar los números primos que hay entre dos números dados \n3. Mostrar el primer número primo mayor que un número dado \n4. Contar y mostrar los primos menores que un número dado \n5. Salir")
#op es opción
op = int(input("..."))
if op == 1:
    print("Opcion 1")
    num = int(input("Ingrese un número: "))
    c = 1
    acum = 0
    while c <= num:
        if num%c == 0:
            acum = acum + 1
        c = c + 1
    if acum == 2:
        print(num, "es primo")
    else:
        print(num, "no es primo")
if op == 2:
    print("Opción 2")
    inf = int(input("Ingrese límite inferior: "))
    sup = int(input("Ingrese límite superior: "))
    if sup or inf > 0:
        for i in range(inf, sup+1):
            acum = 2
            primo = True
            while primo and acum < i:
                if i%acum == 0:
                    primo = False
                else:
                    acum = acum + 1
            if primo:
                print(i, "es primo")
    else:
        print("El número es incorrecto")
if op == 3:
    print("Opción 3")
    def esPrimo(n):
        c = 0
        for i in range(1, n+1):
            if n%i == 0:
                c += 1
        if c == 2:
            return True
        else:
            return False
    def primocercano(n):
        i = n - 1
        near = 0
        while i != 1:
            if esPrimo(i) == True:
                near = 1
                break
            else:
                i = i - 1
        return near
    ###
    num = int(input("Ingrese número: "))
    print(primocercano(num))
if op == 4:
    print("Opción 4")
    flag = True
    acum = 0
    while flag == True:
        num = int(input("Ingrese un número: "))
        if num > 0:
            flag = False
            i = 2
            while i < num:
                creciente = 2
                primo = True
                while primo and creciente < i:
                    if i % creciente == 0:
                        primo = False
                    else:
                        creciente += 1
                if primo:
                    print(i, "es primo")
                    acum = acum + 1
                i = i + 1
        else:
            print("No es primo")
    print("Cantidad de números primos es: ", acum)
if op == 5:
    print("Programa terminado con éxito")