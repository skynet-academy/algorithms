def two_sum(arr, S):
    hash_table = {}
    results = []
    for x in arr:
        if((S - x) in hash_table):
            if(hash_table[S-x]):
                continue
            results.append([x, S - x])
            hash_table[S - x] = True
        else:
            hash_table[x] = False

    return results

print(two_sum([3,5,2,-4,8,11,3,-13,23,5,-6,-10],7))


