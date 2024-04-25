
def longest_string(text):
    word = ""
    longest = ""
    for x in text:
        if(ord(x) != 32):
            word += x
        else:
            print(word, len(word))
            longest = word if len(word) > len(longest) else longest
            word = ""

    print(longest, len(longest))

longest_string("No necesito sustitorio para computacion")
