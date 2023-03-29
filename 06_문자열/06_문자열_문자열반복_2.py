import sys

T = int(sys.stdin.readline())
res = []
for k in range(T):
    S,L = list(map(str , sys.stdin.readline().split()))

    idx = ""
    for i in list(map(str, L)):
        idx += i*int(S)
    res.append(idx)

for p in res:
    print(p)
#%%
