n = int(input())

def print_formated(number):
    i = 0
    hexa_val = ['A', 'B', 'C', 'D', 'E', 'F']
    while(number > i):
        i += 1

        octal = i 
        octal_num = ''
        while(octal > 0):
            octal_num += str(octal % 8)
            octal //= 8

        hexa = i 
        hexa_num = ''
        while(hexa > 0):
            if(hexa % 16 > 9):
                hexa_num  += hexa_val[(hexa % 16) - 10]
            else:
                hexa_num += str(hexa % 16)
            hexa //= 16

        binary = i
        binary_num = ''
        while(binary > 0):
            binary_num += str(binary % 2)
            binary //=2
        
        print(str(i) + " " + octal_num[::-1] + " " + hexa_num[::-1] + " " + binary_num[::-1])

print_formated(n)
