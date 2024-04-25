text1 = input("Enter your text:").split()

def reversing(text1):
    for x in range(len(text1)):
        print(text1[-x-1])

reversing(text1)

