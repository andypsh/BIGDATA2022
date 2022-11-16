import sys


col = 9
A=[]
for i in range(col):
    idx = list(map(int , sys.stdin.readline().split()))
    # [idx[i] for i in range(len(idx))]
    A.append(idx)
#print(A)
maxe = 0
res=[]
for i in range(col):
    #print(max(A[i]))
    if max(A[i]) >= maxe:
        maxe = max(A[i])
        for j in range(9):
            if maxe == A[i][j]:
                res = []
                res.append(maxe)
                res.append([i+1,j+1])

for i in res:
    if type(i) == list:
        for j in i:
            print(j, end = ' ')
    else:
        print(i)

#%%
