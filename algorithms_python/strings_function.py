import sys

N = int(input())
    
arr = []
def operations(key, value, arr):
    switch = {
        'insert': lambda value: arr.insert(value[0], value[1]),
        'remove': lambda value: arr.remove(value[0]),
        'print':  lambda value: print(arr),
        'reverse': lambda value: arr.reverse(),
        'append': lambda value: arr.append(value[0]),
        'pop': lambda value: arr.pop(),
        'sort': lambda value: arr.sort()
        }[key](value)

values = []
for x in sys.stdin:
    values.append((x.strip()).split())

for y in values:
    a = y[0]
    b = list(map(int, y[1::]))
    operations(a, b, arr)

