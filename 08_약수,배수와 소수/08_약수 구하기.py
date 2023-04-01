import sys

N,K = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(1,N+1):
    if N%i == 0:
        res.append(i)
if len(res)>=K:
    print(res[K-1])
else:
    print(0)
#%%
