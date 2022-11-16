import sys
import math

N = int(sys.stdin.readline())

A = []
for i in range(N):
    a = int(sys.stdin.readline())
    A.append(a)
maxs = 1000000001
A= sorted(A)
res = []
maxe = A[-1]
frst = A[0]
d=0
while True:
    maxe = math.gcd(*A)
    if A[0] < maxe:
        for j in range(N):
            A[j]+=maxs
            d=maxs
    else:
        break
    maxs = 1000000001

num = d
#for i in sorted(list(set(res)) , reverse= False):
for i in range(2, num+1):
    if num%i == 0:
        print(i , end=' ')
result = []
# for i in range(2,int(num**0.5)+1):
#     if num%i == 0:
#         result.append(i)
#         result.append(a//i)
# print(*sorted(list(set(result))))

#%%
