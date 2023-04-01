import sys

N,B = list(map(int, sys.stdin.readline().rstrip().split()))
res = []
while N!=0:
    a = N%B
    if a>=10:
        res.append( chr(a+55))
    else:
        res.append(a)
    N = N//B
print(*res[::-1], sep='',end='')

#%%
