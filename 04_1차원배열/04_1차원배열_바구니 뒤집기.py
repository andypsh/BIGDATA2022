import sys

N,M = list(map(int , sys.stdin.readline().split()))


A = [[i+1] for i in range(N)]
# print(A[1:-1:-1]) # index 2 와 1
for i in range(M):
    a,b = list(map(int ,sys.stdin.readline().split()))
    A[a-1:b] = reversed(A[a-1:b])
for i in A:
    print(*i,end=' ')
# [1] [2] [3] [4] [5]

# [2] [1] [3] [4] [5]

# [2] [1] [4] [3] [5]

# [3] [4] [1] [2] [5]