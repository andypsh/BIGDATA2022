import sys

N, M = list(map(int ,sys.stdin.readline().split()))
# N은 바구니 N개, 1부터 N번까지 번호
# print(N,M)


A = [[] for i in range(N)]
# print(A)
for t in range(M):
    i,j,k = list(map(int, sys.stdin.readline().split()))
    for p in range(i-1,j):
        A[p] = k

for i in A:
    if i:
        print(i , end=' ')
    else:
        print(0 , end =' ')
#%%
