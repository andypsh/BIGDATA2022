import sys
import itertools
N, M = map(int , sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split(' ')))

prefix =[0]
prefix_idx  = 0
for i in nums:
    prefix_idx+=i
    prefix.append(prefix_idx)
# print(prefix)


a = list(itertools.combinations_with_replacement([i for i in range(1,6)] , 2))
# b = list(itertools.combinations([i for i in range(1,6)] , 2))
cnt = 0
for i,j in a:
    if (prefix[j] - prefix[i-1]) % M ==0:
        cnt+=1
print(cnt)


#%%
