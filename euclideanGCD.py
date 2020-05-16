#!/usr/bin/python3
"""
calculation of GCD of two numbers using euclidean algorithm
"""
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

def euclidean(a,b):
    while(b):
        a, b =b, a % b
    return print("the GCD {}".format(a))

euclidean(a,b)
