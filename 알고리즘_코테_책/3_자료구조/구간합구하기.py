import sys

T = list(map(int , sys.stdin.readline().rstrip().split(' ')))

M = T[0]

n = T[1]

N = list(map(int , sys.stdin.readline().rstrip().split(' ')))
res , res2 = [0] , []
prefix_sum = 0
for i in range(M):
    prefix_sum += N[i]
    res.append(prefix_sum)
for i in range(n):
    T  = list(map(int , sys.stdin.readline().rstrip().split(' ')))
    res2.append(res[T[1]] - res[T[0] -1])
for i in res2:
    print(i)

