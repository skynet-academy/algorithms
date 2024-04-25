text1 = input("Enter the first letter:")
text2 = input("Enter the second letter:")


def print_string(text1, text2):
    length = len(text1) if len(text1) > len(text2) else len(text2)
    if(len(text1) > len(text2)):
        text2 = text2 + " " * length
    else:
        text1 = text1 + " " * length

    for x in range(length):
        print(f"{text1[x]}\t{text2[x]}")

print_string(text1, text2)
    
