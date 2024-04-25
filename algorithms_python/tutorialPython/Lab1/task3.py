def counting_words(text):
    new_list = {} 
    for x in text:
        if(x in new_list):
            new_list[x] += 1
        else:
            new_list[x] = 1
    return new_list

print(counting_words("hello my friend"))

