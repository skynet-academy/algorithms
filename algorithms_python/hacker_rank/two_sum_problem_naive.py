

def two_sum(arr, S):
    sums = []
    for x in range(len(arr)):
        for y in range(1, len(arr)):
            if(arr[x] + arr[y] == S):
                sums.append([arr[x],arr[y]])

    return sums

print(two_sum([3,5,2,-4,8,11,3,-13,23,5,-6,-10],7))

