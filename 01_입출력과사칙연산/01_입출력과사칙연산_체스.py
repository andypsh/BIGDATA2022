import sys

A = list(map(int, sys.stdin.readline().rstrip().split(' ')))

#킹,퀸,룩,비숍,나이트,폰
B = [1,1,2,2,2,8]
for i in range(len(A)):
    A[i] = B[i]-A[i]
for i in A:
    print(i,end=' ')
#%%

#%%
