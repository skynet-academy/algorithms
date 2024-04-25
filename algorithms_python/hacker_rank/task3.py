import sys

money = sys.stdin.readline().strip().split(" ")
bottle = sys.stdin.readline().strip().split(" ")
b = money[0]
c = money[1]

r = bottle[0]
d = bottle[1]
z = lambda x, y: (10**6)*x + y

purchase = False
bottle = 0

if(z - r < 0):
    if(c > z - r):
        c -= z - r
        d += z - r
        purchase = True
        #if(
        #bottle = z(b, c)/r
        
elif(z - r >= 0):
    if(d > z - r):
        d -= z - r
        c += z - r

