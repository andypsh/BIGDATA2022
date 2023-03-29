import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(" " * (N-i-1) + "*" * (i+1) + "*" * (i))
for j in range(1,N):
    print(" "*(j) + "*"*(N-j) + "*" *(N-j-1))

#%%
