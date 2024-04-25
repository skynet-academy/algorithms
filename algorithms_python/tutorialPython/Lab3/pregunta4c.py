import pregunta3 as mate

def demo(a,n):
    pt = mate.potencia(a,n)
    ft = mate.factorial(n)
    print(pt, ft)
    if pt < ft:
        print("Cumple la propiedad")
    else:
        print("No cumple la propiedad")
num = int(input("Ingrese un número: "))
pot = int(input("Ingrese potencia: "))
demo(num, pot)