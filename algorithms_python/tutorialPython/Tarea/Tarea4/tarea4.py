# Pregunta 1
def grado(p):
    return len(p) - 1

# Pregutna 2
def evaluar(poli, x):
    resultado = poli[0]
    for i in range(1, len(poli)):
        resultado = resultado + poli[i] * x ** i
    return resultado

# Pregunta 3
def sumar_poli(poli1, poli2):
    
    size = max(len(poli1),len(poli2))
    suma = [0 for i in range(size)]
    
    for i in range(0, len(poli1), 1):
        suma[i] = poli1[i]
    for i in range(len(poli2)):
        suma[i] += poli2[i]
    
    return suma

# Pregunta 4 
def derivar_polinomio(poli):
    # multiply coeficient with exponet
    coef = poli
    exp = []
    for i in range(1, len(poli), 1):
        if coef[i] == 0:
            exp = exp + [0]
        else:
            exp = exp + [coef[i]*i]
    return exp

# Pregunta 5
def multiplicar_polinomios(poli1,poli2):
    #size = max(len(poli1),len(poli2))
    prod = []
    prod_len = len(poli1) + len(poli2) - 1
    for i in range(prod_len):
        prod.append(0)
    for i in range(len(poli1)):
        for j in range(len(poli2)):
            prod[i+j] += poli1[i] * poli2[j]
    return prod

# Pregunta 6
def mean_of_lists(a,b,c):
    max_length = max(len(a), len(b), len(c))
    [a.append(0) for x in range(max_length - len(a))]
    [b.append(0) for y in range(max_length - len(b))]
    [c.append(0) for z in range(max_length - len(c))]
    average = []
    div = lambda nro: 1 if nro != 0 else 0
    [average.append(int((a[x] + b[x] + c[x])/ \
                    (div(a[x]) + div(b[x]) + div(c[x]))))\
                    for x in range(max_length)]
    return average

# Pregunta 7
refs  = {"Normal": [3000,4000] , "Extra": [7000, 500], "Super": [2000, 600]}
compts = {"Normal": [10,15,18], "Extra": [5,4,2], "Super": [35,31,30]}

def totales_anuales(a, b):
    #totales_aceites = dict([[x, sum(y)] for x,y in refs.items()])
    totals = {}
    for x,y in compts.items():
        totals[x] = [m*sum(refs[x]) for m in y]

    return totals

print(totales_anuales(refs, compts))


def maximo_alquitran(a,b):
    alquitran = [y[1] for x, y in compts.items()]
    max_alquitran = {x:sum(y)*a for x,y in refs.items() for a in alquitran}
    print(max_alquitran)

print(maximo_alquitran(refs, compts))