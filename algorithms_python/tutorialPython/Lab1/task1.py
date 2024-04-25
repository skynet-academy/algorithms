import random
def generator():
    count = 0
    while(True):
        letter = chr(random.randint(97, 122)) 
        print(letter,end="")
        if(letter == 'w'):
            count+=1 
            if(count == 20):
                break
    return count

print(generator())
