import sys

N = int(sys.stdin.readline())
A=[]
for i in range(N):
    a = list(map(int, (sys.stdin.readline().split())))
    A.append(a)

res = [1 for i in range(N)]

for i in range(len(A)):
    for j in range(1,len(A)-i):
        if A[i][0] < A[i+j][0] and A[i][1] < A[i+j][1]:
            print(A[i][0] , "<" , A[i+j][0])
            print(A[i][1] , "<" , A[i+j][1])
            res[i]+=1
        elif A[i][0] > A[i+j][0] and A[i][1] > A[i+j][1]:
            res[i+j]+=1
        # else:
            # print('=======')
            # print(A[i][0] , ">=" , A[i+j][0])
            # print(A[i][1] , ">=" , A[i+j][1])
for i in res:
    print(i , end = ' ')
#%%
