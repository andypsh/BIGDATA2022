import sys

N = map(int , sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(set(A)-set(B))
D = list(set(B)-set(A))
print(len(C)+ len(D))
#%%
