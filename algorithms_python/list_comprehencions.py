"""

given three integers x,y, and z, representing the dimensions of a cuboid along with an integer. 
Print a list of all possible coordinates given by(i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.
Here, 0<= i <=x; 0<=j <= y; <=k <=z. 



x = 1, y = 1, z = 2, n = 3
all permutations of [i, j, k] are:
    [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], 
     [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]

Algorithm that the elements that do not sum to n = 3

    result [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]] 


"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())

x = list(range(x+1))
y = list(range(y+1))
z = list(range(z+1))

perm = [[i,j, k] for i in x for j in y for k in z]
print([a for a in perm if(sum(x for x in a) != n)])


