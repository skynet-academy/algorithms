import random

def matriz(n, m):
    l = []
    for f in range(n):
        l.append([])
        for c in range(m):
            l[f].append(random.randint(-10, 10))
    return l

def imp_matriz(B):
    for i in range(len(B)):
        print()
        for j in range(len(B[i])):
            print(B[i][j], end=" ")

