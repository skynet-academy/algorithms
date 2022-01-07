
a = int(input())
set_a = set(map(int, (input().split())))
b = int(input())
set_b = set(map(int, (input().split())))
print(a, set_a, b, set_b)
for x in set_a.symmetric_difference(set_b):
    print(x)
