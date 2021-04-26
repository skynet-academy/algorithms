#!/usr/bin/python3


def merge(A, p, q, r):

    n1 = q - p + 1
    n2 = r - q

    # subarrays
    L = [0]*n1
    M = [0]*n2
    
    for x in range(n1):
        L[x] = A[p + x]
    for y in range(n2):
        M[y] = A[q + 1 + y]

    x = 0
    y = 0
    k = p

    while(x < n1 and y < n2):
        if(L[x] <= M[y]):
            A[k] = L[x]
            x+=1
        else:
            A[k] = M[y]
            y+=1
        k+=1

    while(x < n1):
        A[k] = L[x]
        x+=1
        k+=1

    while(y < n2):
        A[k] = M[y]
        y+=1
        k+=1


def sort(A,p,r):
    if(p < r):
        q = (p + r)//2
        sort(A, p, q)
        sort(A, q + 1, r)
        merge(A, p, q, r)


A = [5, 2, 4, 6, 1, 3, 2, 6]

sort(A, 1 , len(A))


