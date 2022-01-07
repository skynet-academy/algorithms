s = input()

letters_count = {}

for x in s:
    if(x in letters_count):
        letters_count[x] += 1
    else:
        letters_count[x] = 1

dict_ordered = {k: v for k, v in sorted(letters_count.items(), key=lambda item: item[1])}
count = 0

while(count < 3):
    last = list(dict_ordered)[-1]
    previous_last = list(dict_ordered)[-2]
    if(dict_ordered[last] > dict_ordered[previous_last]):
        print(*dict_ordered.popitem())
    else:
        dict_ordered
        print(*dict_ordered.popitem())
    count +=1 

