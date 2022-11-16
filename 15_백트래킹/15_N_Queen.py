import sys
import itertools

N = int(sys.stdin.readline())
#A=[[] for i in range(N)]

for i in range(N):
    A = [i for i in range(N)]
print(A)
#A[0][0]=True
# for i in range(N):
#     for j in range(N):
#         A[i][j]=
#         else:
#             A[i][j] = True

array = itertools.combinations_with_replacement(A,2)
b=0
for i in array:
    for j in i:
        print(j,end=' ')
    b+=1
    print()
print(b)

#%%
