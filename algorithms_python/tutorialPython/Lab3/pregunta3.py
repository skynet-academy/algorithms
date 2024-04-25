#3a
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
#3b
def potencia(base, exp):
    if exp == 0:
        return 1
    if base == 0:
        return 0
    if exp < 0:
        return 1/base*potencia(base, exp+1)
    if exp == 1:
        return base
    else:
        return base * potencia(base, exp-1)
