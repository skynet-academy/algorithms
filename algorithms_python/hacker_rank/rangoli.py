n = int(input())


def print_rangoli(size):
    center = '' 
    i = 0
    while(size > i):
        i += 1
        pos = size - i
        center += chr(97 + pos)
        left = '-'.join(center)
        right = '-'.join(center[::-1])[1:]

        print("--"*pos + left + right + "--"* pos)
    while(i > 1):
        i -= 1
        pos = size - i
        left = left[:-2]
        right = right[2:]
        print("--"*pos + left + right + "--"* pos)

print_rangoli(n)
