import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

B = int(sys.stdin.readline())
C = {}
for i in A:
    if i in C.keys():
        C[i] +=1
    else:
        C[i] =1
if B in C.keys():
    print(C[B])
else:
    print(0)
#%%
