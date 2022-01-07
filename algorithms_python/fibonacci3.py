#def fibonacci(n):
#    fib_num = []
#    if(n == 0):
#        return fib_num.append(n)
#    else:
#        while(len(fib_num) < n):
#            fib_num.append(map(lambda x: x % 2 == 0, fib_num))
#

list(map(lambda x: a.remove(x) if (x % 2 != 0) else False , a))
num_fib = [0,1]

def fib(n):
    num_fib.append(num_fib[-1] + num_fib[-2]) 
    if((num_fib[-1] + num_fib[-2]) % 2 == 0):
        
