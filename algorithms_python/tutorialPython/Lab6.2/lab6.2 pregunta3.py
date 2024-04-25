import random

def SeparaMemoria(N,M):
    A=[None]*N
    for f in range(N):
        A[f]=[None]*M
    return A

#print(A)
def LlenarMatriz(A,N,M):
    for f in range(N):
        for c in range(M):
            A[f][c]=random.randint(0,20)
    return A



def MostrarMatriz(A,N,M):
    for f in range( len(A) ):
        for c in range(M):
            print("%5d"%A[f][c],end=" ")
        print()

N=10
M=5
A=SeparaMemoria(N,M)
LlenarMatriz(A,N,M)
MostrarMatriz(A,N,M)

for f in range(0,N):
    sf=0
    print("Estudiante %d"%(f+1),end=" ")
    for c in range(0,5):
        print("%5d"%A[f][c],end=" ")
        sf+=A[f][c]
    #promedio es la suma de notas entre 5 (examenes)
    print("%7.1f"%(sf/5))
    print()



#Datos de resumen

print("Resumen "+" "*4,end="")
st=0
for c in range(0,5):
    sc=0
    for f in range(0,N):
        sc+=A[f][c]
    st=st+sc/N
    print("%6.1f"%(sc/N),end="")    
print()

