def reduceS(s, idx, letter):
    s = ''.join([s[x] if x != idx else letter for x in range(len(s))])
    s = ''.join([s[x] if x != idx + 1 else '' for x in range(len(s))])

    return s


def stringTransform(s):
    idx = 0
    swap = True
    while(swap):
        while(idx < len(s) - 1):
            swap = False
            if(s[idx] == s[idx + 1]):
                idx += 1
            else:
                if(s[idx] == 'a'):
                    if(s[idx + 1] == 'b'):
                        s = reduceS(s, idx, 'c')
                    elif(s[idx + 1] == 'c'):
                        s = reduceS(s, idx, 'b')
                    idx = idx + 1
                    swap = True

                elif(s[idx] == 'b'):
                    if(s[idx + 1] == 'a'):
                        s = reduceS(s, idx, 'c')
                    elif(s[idx + 1] == 'c'):
                        s = reduceS(s, idx , 'a')
                    idx = idx + 1
                    swap = True
                elif(s[idx] == 'c'):
                    if(s[idx + 1] == 'a'):
                        s = reduceS(s, idx, 'b')
                    elif(s[idx + 1] == 'b'):
                        s = reduceS(s, idx , 'a')
                    idx = idx + 1
                    swap = True
        if(len(s) == 1):
            swap = False
        idx = 0
        if(not swap):
            break
    return len(s)

print(stringTransform(input()))
