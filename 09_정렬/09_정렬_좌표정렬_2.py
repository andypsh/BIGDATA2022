import sys

N = int(sys.stdin.readline())
res = []
for i in range(N):
    a = list(map(int ,sys.stdin.readline().rstrip().split()))
    idx = a[0]
    a[0] = a[1]
    a[1] = idx

    res.append(a)


res = sorted(res)
for i in res:
    idx = i[0]
    i[0] = i[1]
    i[1] = idx
    for p in i:
        print(p , end=' ')
    print('')
#%%
