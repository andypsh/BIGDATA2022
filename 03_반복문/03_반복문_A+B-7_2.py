import sys

T = int(sys.stdin.readline())
res = []
for i in range(T):
    A = list(map(int, sys.stdin.readline().split()))
    res.append(A[0]+A[-1])
for j in range(T):
    print(f"Case #{j+1}: {res[j]}")



#%%
