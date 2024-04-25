from pregunta3 import factorial,potencia

def demo(a,n):
    pt = potencia(a,n)
    ft = factorial(n)
    print(pt, ft)
    if pt < ft:
        print("Cumple la propiedad")
    else:
        print("No cumple la propiedad")
num = int(input("Ingrese un número: "))
pot = int(input("Ingrese potencia: "))
demo(num, pot)