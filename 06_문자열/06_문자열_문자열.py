import sys

T = int(sys.stdin.readline())
res = []
for i in range(T):
    s = list(sys.stdin.readline().rstrip())
    res.append(s[0]+s[-1])

for k in res:
    print(k)
#%%
