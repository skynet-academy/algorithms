def replace(text):
    new_text =[]
    for x in text:
        if(48<= ord(x) <= 57):
            new_text.append(chr(ord(x) - 1) if ord(x) != 48 else chr(ord(x) + 9))
        elif(97 <= ord(x) <= 122):
            new_text.append(chr(ord(x) + 1) if ord(x) != 122  else chr(ord(x) - 25))
        else:
            new_text.append(x)
    return new_text


print(*replace("hello0 my1 friendz"))
