import sys

numbers = sys.stdin.readline()
def sum(numbers):
    a = numbers.split(" ")
    a[-1] = a[-1].strip()
    return int(a[0]) + int(a[1])

print(sum(numbers))
