import sys
import copy

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().rstrip().split()))
S = {}
res = {}
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(len(B)):
    S[B[i]] = 0
#     res[i] = 0
#print(S.get(16))
res = copy.deepcopy(S)
for i in A:
    if S.get(i) is not None:
        #print('good')
        res[i] +=1
for i in B:
    print(res.get(i) , end = ' ')
#%%
