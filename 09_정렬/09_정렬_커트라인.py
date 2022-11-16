import sys


N = list(map(int, sys.stdin.readline().split()))

A = list(map(int, sys.stdin.readline().split()))

b = sorted(A , reverse = True)
print(b[N[1]-1])

#%%

#%%
