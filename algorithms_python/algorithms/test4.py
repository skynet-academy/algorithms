def missingCharacters(s):
    # Write your code here
    numbers = []
    letters = []
 
    [numbers.append(int(x)) if x.isnumeric() else letters.append(x) for x in s]
    
    new_numbers = []
    new_letters = []
    [new_numbers.append(x) if x not in numbers else x for x in list(range(10))]
    [new_letters.append(chr(x)) if chr(x) not in letters else x for x in list(range(97,123))]
    sorted(new_letters)
    sorted(new_numbers)
    new_numbers = list(map(str, new_numbers))
    return ''.join(new_numbers) + ''.join(new_letters)
    

print(missingCharacters(input()))
