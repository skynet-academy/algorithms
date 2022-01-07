#!/usr/bin/python3

def factorial(nro):
    fac = 1
    n = 1
    while(nro > fac):
        fac *= n
        if(fac < nro):
            n+=1
        else:
            break

    print("{} is the closest number to {}, {} is the times we multiply it".format(fac, nro, n))

factorial(1000000)

