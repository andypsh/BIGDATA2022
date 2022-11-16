import sys


N = list(map(int, sys.stdin.readline().rstrip().split()))
S = {}
for i in range(1,N[0]+1):
    S[i] = sys.stdin.readline().rstrip()
T ={v:k for k,v in S.items()}
res = []
for j in range(N[1]):
    a = sys.stdin.readline().rstrip()
    if a.isnumeric():
        res.append(S.get(int(a)))
    else:
        res.append(int(T.get(a)))
for i in res:
    print(i)
#%%
