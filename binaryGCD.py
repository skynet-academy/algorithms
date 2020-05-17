#!/usr/bin/python3

"""
Binary gcd is an algorithm that finds the GCD of two numbers by repeatedly applying the following
identities:
    gcd(0,b) = b
    gcd(a,0) = a
    gcd(0,0) = 0
    if 'a' and 'b' are both even, so gcd(a,b) = 2gcd(u/2,v/2) , because 2 is a common divisor
    if 'a' is even and 'b' is odd, then gcd(a/2,b), because 2 is not a common divisor
    if 'a' is odd and 'b' is even, then gcd(a,b/2), because 2 is not a common divisor
    if 'a' and 'v' are both odd, and a>=b, then gcd(a,b)= gcd((a-b)/2, b)
    if both are odd and a<b, then gcd(a,b)= gcd((b-a)/2)

    Repeat steps 2-4 until a = b, or one more step until a = 0.
    The GCD is 2^k*b, where k = number common factors of 2
"""


def binaryGCD():
    try:
        a = int(input("Enter the first number: \n"))
    except ValueError:
        print("this is not an integer")
    try:
        b = int(input("Enter the second number: \n"))
    except ValueError:
        print("This is not an integer")
    d = 0
    while(a%2==0 and b%2==0):
        a //=2
        b //=2
        d+=1
    while(a!=b):
        if(a%2==0):
            a//=2
        elif(b%2==0):
            b//=2
        elif(a>b):
            a =(a-b)//2
        else:
            b =(b-a)//2
    g = a
    print("the binary GCD is {}".format(g*(2**d)))


binaryGCD()
