from itertools import groupby

numbers = input()

for x, y in groupby(numbers):
    print((len(list(y)), int(x)), end=" ")
