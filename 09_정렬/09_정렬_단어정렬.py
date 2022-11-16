import sys

A = int(sys.stdin.readline())
res = []
for i in range(A):
    a = list(str(sys.stdin.readline().rstrip()))
    b= len(a)
    a.append(b)
    res.append(a)

res = list(set(map(tuple,res)))

res.sort(key = lambda x : (x[-1] , x[0:-1] ))


for i in res:
    for p in i[:-1]:
        print(p , end = '')
    print('')
#%%
