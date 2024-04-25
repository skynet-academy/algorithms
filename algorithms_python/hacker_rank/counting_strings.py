length = int(input())
strings = {}

for x in range(length):
    word = input()
    if(word in strings):
        strings[word] += 1
    else:
        strings[word] = 1

print(len(strings))
print(*[strings[x] for x in strings])
