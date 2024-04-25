from collections import OrderedDict

ord_dict = OrderedDict()

for _ in range(int(input())):
    product = input().split()
    name = ' '.join(product[:-1:])
    price = int(product[-1])
    if(name in ord_dict):
        ord_dict[name] += price
    else:
        ord_dict[name] = price

for key, value in ord_dict.items():
    print(key + " " + str(value)) 
