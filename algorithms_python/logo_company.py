strings = input()
words = {}
for x in strings:
    if(x in words):
        words[x] += 1
    else:
        words[x] = 1
groups = {}
for key, value in words.items():
    if(value in groups):
        groups[value] += key
    else:
        groups[value] = key

groups = {k: sorted(v) for k, v in sorted(groups.items())}
counter = 0
while(counter < 3):
    if(len(groups)>1):
        last = list(groups)[-1]
        bef_last = list(groups)[-2]
        if(last > bef_last):
            if(len(groups.get(last)) == 1):
                print(*groups.get(last)[0], last)
                groups.popitem()
                counter += 1
            else:
                print(*groups.get(last).pop(0), last)  
                counter += 1
    else:
        last = list(groups)[-1]
        print(*groups.get(last).pop(0), last)
        counter += 1
