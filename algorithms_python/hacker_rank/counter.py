from collections import Counter

size = int(input())
items = Counter(map(int, input().split(" ")))
total_purchase = 0
for _ in range(int(input())):
    item, price = input().split(" ")
    if(items[int(item)] > 0):
        total_purchase += int(price)
        items[int(item)] -= 1

print(total_purchase)



