import sys
import copy

A = list(map(int , sys.stdin.readline().split(' ')))

B = list(map(int ,sys.stdin.readline().split(' ')))

C = copy.deepcopy(B)
res =[]
#print(C)
max3 =0
for k in range(len(B)):
    for i in range(k,A[0]-1):
        B[i+1] += B[i]
    # for j in range(k,0,-1):
    #     B[j-1] = B[j]+B[j-1]
    # print('B : {}'.format(B))

    if len(B[k:])>=A[1]:
        # print('B의 {}번째 : {}'.format(k , B[k:][A[1]-1]))
        # print('==')
        if max3 < B[k:][A[1]-1]:
            max3 = B[k:][A[1]-1]
    B = copy.deepcopy(C)
print(max3)


# print(C)
#
# print(res)
# print(max(res))
# for i in res:
#     if len(i)>= A[1]:
#         if max<i[A[1]-1]:
#             max = i[A[1]-1]
# print(max)
#for j in range(1,A[0]-1):
#    C[j+1] += C[j]

#print(C[1:])
#%%

#%%
