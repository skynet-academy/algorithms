[n, m] = list(map(int, input().split()))

my_list = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
def happiness_calculator(my_list, set_a, set_b):
    global happiness
    likes = sum(list(map(lambda x: 1 if x in set_a else 0, my_list)))
    dislikes = sum(list(map(lambda x: -1 if x in set_b else 0, my_list)))
    happiness = likes + dislikes
    return happiness

#if(1 <= n <= 10.E+4 and 1 <= m <= 10.E+4 and 1<= len(my_list) <= 10.E+4):
print(happiness_calculator(my_list, set_a, set_b))
