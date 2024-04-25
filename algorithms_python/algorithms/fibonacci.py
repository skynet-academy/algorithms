def f(n):
    fib_nums = [0,1]
    for x in range(n - len(fib_nums)):
        fib_nums.append(fib_nums[x] + fib_nums[x+1]) 
    print(fib_nums)

f(4)
def f2(n):
    fib_nums = [0] 
    n2 = 1 
    n1 = n2 - 1 
    while(len(fib_nums) < n):
        result = n1 + n2
        if(result % 2 == 0):
            fib_nums.append(result)
        n1 = n2
        n2 = result
    return fib_nums
print(f2(4))

#fib_numbs = [0,1]
#def fib(n):
#    print(n)
#    n1 = n
#    d1 = fib_numbs[-2]
#    d2 = fib_numbs[-1]
#    fib_numbs.append(d1 + d2)
#    if(len(fib_numbs) > n1):
#        return  
#    else:
#        fib(n - 1)
#fib(6)
#print(fib_numbs)
#


