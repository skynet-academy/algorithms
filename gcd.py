#!/usr/bin/python3
import sys

"""
calculating the greatest common divisor using recursivity
"""

a = int(sys.argv[1])
b = int(sys.argv[2])


def gcd(a,b):
    if (b == 0): 
        return print("the gcd is: {} ".format(a))
    else:
        
        return gcd(b, a%b)

gcd(a,b)


