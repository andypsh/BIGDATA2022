import sys

n = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
m = int(sys.stdin.readline())
E = list(map(int, sys.stdin.readline().rstrip().split()))
A = [0 for i in range(20000001)]

for i in range(len(D)):
    A[D[i]+10000000] += 1

for j in E:
    print(A[j+10000000] , end =' ')


#%%
