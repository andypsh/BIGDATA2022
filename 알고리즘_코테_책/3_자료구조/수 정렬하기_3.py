import sys

N = int(sys.stdin.readline())

A = [0]*10001

for i in range(N):
    a = int(sys.stdin.readline())
    A[a] += 1
# print(A.index(2))
for i in range(10001):
    if A[i] != 0:
        for _ in range(A[i]):
            print(i)
#%%
