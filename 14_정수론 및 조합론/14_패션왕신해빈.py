import sys

def fact(n):
    res = 1
    if n==1 or n==0:
        return 1
    else:
        for i in range(n,1, -1):
            res*=i
        return res
print(fact(5))
M = int(sys.stdin.readline())
res = []
for k in range(M):
    N = int(sys.stdin.readline())
    B = {}
    for i in range(N):
        A = list(map(str, sys.stdin.readline().split()))

        if A[1] in B.keys():
            B[A[1]] += 1
        else:
            B[A[1]] = 1
    #print(B)
    count = 1
    for key in B.keys():
        count *= B[key] +1
    res.append(count-1)
for i in res:
    print(i)

#%%
