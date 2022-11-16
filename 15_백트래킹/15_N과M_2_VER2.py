import itertools
import sys

n,m = map(int, sys.stdin.readline().split())

res = [i for i in range(1,n+1)]

array = itertools.permutations(res, m)
for i in array:
    for j in i:
        print(j , end = ' ')
    print()
#%%
