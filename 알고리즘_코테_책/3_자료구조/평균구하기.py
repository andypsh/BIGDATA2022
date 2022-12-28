import sys
import itertools

a = int(sys.stdin.readline())

b = list(map(int, sys.stdin.readline().rstrip().split(' ')))

chng = max(b)

all , res = 0 ,0
res = (sum(b) /chng*100) / len(b)
print(res)
#%%

#%%
