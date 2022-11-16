# import sys
# import math
# #
# N = list(map(int , sys.stdin.readline().split()))
# sume = []
# 
# for i in range(N[0] , N[1]+1):
#     if i== (2 or 3):
#         sume.append(i)
# 
#     else:
#         a = math.sqrt(i)

M, N = map(int, input().split())
arr = [True] * (N + 1)
prime = []
for i in range(N+1):
    if i == 1 or i == 0:
        continue
    elif arr[i]:
        prime.append(i)
        for j in range(2 * i, N + 1, i):
            arr[j] = False

for i in prime:
    if i >= M:
        print(i)
#%%
