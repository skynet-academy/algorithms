num = []

def fibonacci(n):
    f1 = 0
    f2 = 1
    i = 0
    while(i < n):
        if(f1 == 0):
            #num.append(f1)
            print(f1, end=",")
            i+=1
        f1 = f2
        f2 = f1 + f2
        if(f2 % 2 == 0):
            print(f2, end=",")
            #num.append(f2)
            i +=1
        if(len(num) == n):
            break
    print("\n")



    
fibonacci(4)
fibonacci(5)
fibonacci(-6)
fibonacci(10)
