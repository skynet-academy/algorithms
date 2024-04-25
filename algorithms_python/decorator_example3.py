import math

from decorator_example2 import debug

# applying a decorator to a standar library function

math.factorial = debug(math.factorial)
def approximate_e(terms=18):
    return sum(1/math.factorial(n) for n in range(terms))


a = approximate_e(10)
print(a)
