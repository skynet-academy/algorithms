
def fibonacci(n):
    num_fib = [] 
    n0 = 0
    n1 = 1
    a = 0 
    while(len(num_fib) < n):
        if(a % 2 == 0):
            num_fib.append(a)
        n0 = n1
        n1 = a 
        a = n0 + n1
    num_fib = ", ".join(map(str, num_fib))

    return num_fib


       


print(fibonacci(4))

#   fibonacci = lambda n: n if n<= 1 else (fibonacci(n - 1) + fibonacci(n - 2))
#
#def fibonacci(n):
#    return (n if n <= 1 else (fibonacci(n -1) + fibonacci(n - 2)))




