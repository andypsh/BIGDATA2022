import sys

T = int(sys.stdin.readline())

res = []
for i in range(T):
    A = list(map(int , sys.stdin.readline().split()))
    res.append(f"Case #{i+1}: {A[0]} + {A[-1]} = {A[0] +A[-1]}")
for j in range(T):
    print(res[j])
#%%
