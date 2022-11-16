import sys

n = int(sys.stdin.readline())
b = [[0 for i in range(101)] for j in range(101)]
# print(b)
for i in range(n):
    A = list(map(int ,sys.stdin.readline().split()))
    for k in range(A[1], A[1]+10):
        for p in range(A[0] , A[0]+10):
            b[k][p] = 1
res = 0
for i in b:
    res += i.count(1)
print(res)

#%%
