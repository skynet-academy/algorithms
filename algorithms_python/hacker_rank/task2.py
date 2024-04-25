import sys

j = sys.stdin.readline().strip()
s = sys.stdin.readline().strip()


result = 0

for x in s:
    if x in j:
        result += 1

print(result)
