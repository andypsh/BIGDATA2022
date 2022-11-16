import sys

N = int(sys.stdin.readline())
res , res_x , res_y =[] , [] , []
for i in range(N):
    a = list(map(int ,sys.stdin.readline().rstrip().split()))
    res.append(a)
    res_x.append(a[0])
    res_y.append(a[1])

res = sorted(res)
for i in res:
    for p in i:
        print(p , end=' ')
    print('')

#%%
