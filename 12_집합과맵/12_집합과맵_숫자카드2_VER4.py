import sys
import copy

#N = int(sys.stdin.readline())

A = map(int, sys.stdin.readline().split())
S = {}
res = {}
# M = int(sys.stdin.readline())
B = map(int, sys.stdin.readline().split())

C = copy.deepcopy(B)
for i in B:
    S[i] = 0
res = copy.deepcopy(S)
for i in A:
    if S.get(i) is not None:

        res[i] +=1

for i in C:
    #print("i:i)
    print(res.get(i) , end = ' ')
#%%
