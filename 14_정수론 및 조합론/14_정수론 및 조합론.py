import sys

res = []
while True:
    A= list(map(int, sys.stdin.readline().rstrip().split()))
    if A == [0,0]:
        break
    if A[0]<A[1]:
        if A[1]%A[0]==0:
            res.append('factor')
        else:
            res.append('neither')
    else:
        if A[0]%A[1]==0:
            res.append('multiple')
        else:
            res.append('neither')
for i in res:
    print(i)
#%%
