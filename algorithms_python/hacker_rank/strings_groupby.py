from itertools import groupby

string, k = input(), int(input())

def merge_the_tools(string, k):
    for x in range(k):
        sub_string = string[:k]
        print(sub_string)
        string = string[k: len(string)]
        #print(''.join([x for x,y in groupby(sub_string)]))

merge_the_tools(string, k)

