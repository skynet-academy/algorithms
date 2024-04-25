import operator

def person_lister(f):
    def inner(people):
        value = [[int(x[2]),f(x)] for x in people]
        swapped = True
        while(swapped):
            swapped = False
            for x in range(len(value) - 1):
                if(value[x][0] > value[x+1][0]):
                    value[i], value[x+1] = value[x+1], value[x]
                    swapped = True
        return [x[1] for x in value]
        # complete the function
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
