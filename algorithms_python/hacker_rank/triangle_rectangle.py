import math 
side1 = int(input())
side2 = int(input())

c = math.sqrt(side1 ** 2 + side2 ** 2)
cos = side2/c
degrees = (math.acos(cos)*180)/math.pi
print(str(round(degrees)) + u'\N{DEGREE SIGN}')
