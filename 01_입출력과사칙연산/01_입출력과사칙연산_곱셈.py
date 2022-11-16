import sys

A = int(sys.stdin.readline())
B = list(map(int , sys.stdin.readline().rstrip()))
C=[]
for i in range(1,len(B)+1):
    C.append(A*B[-i])
for j in range(len(C)):
    print(C[j])
    C[j] = C[j]*(10**(j))

print(sum(C))



#%%
