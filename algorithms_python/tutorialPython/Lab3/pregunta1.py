def max1(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    return n3
n1 = int(input("Ingrese primer valor: "))
n2 = int(input("Ingrese segundo valor: "))
n3 = int(input("Ingrese tercer valor: "))
print(max(n1,n2,n3))
