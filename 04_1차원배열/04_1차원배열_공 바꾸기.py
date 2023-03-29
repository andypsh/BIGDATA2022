import sys

N,M= list(map(int, sys.stdin.readline().split()))

A = [[i+1] for i in range(N)]

for k in range(M):
    i,j = list(map(int, sys.stdin.readline().split()))
    idx = A[i-1]
    A[i-1] = A[j-1]
    A[j-1] = idx
    # print(f"{k+1}번째 :{A}")

for i in A:
    print(*i , end = ' ')


#A = [2] [1] [3] [4] [5]
#A = [2] [1] [4] [3] [5]
#A = [3] [1] [4] [2] [5]

#%%
