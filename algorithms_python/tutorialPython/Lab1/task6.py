text1 = input("first text:")
text2 = input("second text:")


def concatenate(text1, text2):
    return text2[:2:] + text1[2:] + " " + text1[:2:] + text2[2:]

print(concatenate(text1, text2))

