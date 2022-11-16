import sys

A = list(map(int , sys.stdin.readline().split(' '))) #N = 개수 , M= 합을 구해야 하는 횟수
B = list(map(int , sys.stdin.readline().split(' '))) #N개의 개수
res= []
# for i in range(A[1]):
#     C = list(map(int, sys.stdin.readline().split(' ')))
#     a = sum(B[C[0]-1:C[1]])
#     res.append(a)
# for i in res:
#     print(i)

for i in range(A[0]-1):
    #B= [5,4,3,2,1]
    B[i+1] += B[i] #B[1] += B[0] = [5,9,3,2,1]
    #B[2] += B[1] = [5,9,12,2,1]
    #B[3] += B[2] = [5,9,12,14,1]
    #B[4] += B[3] = [5,9,12,14,15]
B = [0] + B
#B = [0,5,9,12,14,15]
for i in range(A[1]):
    C = list(map(int, sys.stdin.readline().split(' ')))
    res.append(B[(C[1])] - B[(C[0]-1)])
for j in res:
    print(j)

#%%
