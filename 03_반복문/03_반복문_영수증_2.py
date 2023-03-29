import sys

X = int(sys.stdin.readline())

N = int(sys.stdin.readline())
res = 0
for i in range(N):
    A = list(map(int , sys.stdin.readline().split()))
    res += A[0]*A[-1]

if res == X:
    print('Yes')
else:
    print('No')
#%%
