import sys

N = list(map(int, sys.stdin.readline().rstrip().split()))
A_1 , B_1 =[] , []
for i in range(N[0]):
    A=list(map(int ,sys.stdin.readline().split()))
    A_1.append(A)
for j in range(N[0]):
    B=list(map(int ,sys.stdin.readline().split()))
    B_1.append(B)
res =[]
for i in range(N[0]):
    idx = []
    for j in range(N[1]):
        a = A_1[i][j] + B_1[i][j]
        idx.append(a)
    res.append(idx)
for i in range(N[0]):
    for j in range(N[1]):
        print(res[i][j] , end=' ')
    print()
#%%

#%%
