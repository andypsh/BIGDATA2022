import sys
import itertools
N, M = map(int , sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split(' ')))

prefix = [0] * N
prefix[0] = nums[0]
answer = 0
C = [0]* M

for i in range(1, N):
    prefix[i] = prefix[i-1] + nums[i]
for i in range(N):
    remainder = prefix[i] % M
    if remainder == 0:
        answer+= 1

    C[remainder] += 1

for i in range(M):

    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) //2)

print(answer)


#%%
