import math
import sys

T = int(sys.stdin.readline())
res = []
for i in range(T):
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    a = A[0]*A[1]//math.gcd(A[0],A[1])
    res.append(a)

for i in res:
    print(i)
#%%
