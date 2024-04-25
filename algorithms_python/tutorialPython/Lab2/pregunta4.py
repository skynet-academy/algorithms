cad1=input("Enter string 1:")
cad2=input("Enter string 2:")
c = 0
for i in cad1:
    for j in cad2:
        if i == j:
            c = c+1
if c == len(cad1) and c == len(cad2):
    print("Son anagramas.")
else:
    print("No son anagramas.")