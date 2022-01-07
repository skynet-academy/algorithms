from collections import deque

length = int(input())

d = deque()

for x in range(length):
    operation = input().split()
    if(operation[0] == "append"):
        d.append(int(operation[1]))
    elif(operation[0] == "appendleft"):
        d.appendleft(int(operation[1]))
    elif(operation[0] == "pop"):
        d.pop()
    elif(operation[0] == "popleft"):
        d.popleft()

print(*[x for x in d])





