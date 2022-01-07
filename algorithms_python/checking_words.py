a,b = input().split()
words_a = {} 
for x in range(1, int(a) + 1):
    word = input()
    words_a[x] = word 


for y in range(int(b)):
    word = input()
    if(word in words_a.values()):
        print(*[key for key,  value in words_a.items() if value == word])
    else:
        print(-1)


