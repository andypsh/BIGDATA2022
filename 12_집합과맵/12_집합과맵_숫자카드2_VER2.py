import sys
import copy

N = int(sys.stdin.readline())

A = map(int, sys.stdin.readline().split())
S = {}
res = {}
M = int(sys.stdin.readline())
B = map(int, sys.stdin.readline().split())
for i in B:
     S[i] = 0
#     res[i] = 0
#print(S.get(16))
res = copy.deepcopy(S)
for i in A:
    if S.get(i) is not None:
        #print('good')
        res[i] +=1

for i in B:
    print(res.get(i) , end = ' ')


# for i in B:
#     if S.get(i) is not None : #key 가 6이면  value값 출력
#     #print('good')
#         S[i] += 1
#     else:
#         continue
# print(S)
# print(res)
#S = {v:k for k,v in S.items() }


# for i in B:
#     if S.get(i):
#         print(i)
#         res[i] +=1
# print(res)
# for i in B:
#     if (k for k,v in S.items() if k==i):
#         res[i] += 1
# print("res : {}".format(res))
# for i in M:
#     if S.get(i):
#         res[i]+=1
#     else:
#         continue
# T ={v:k for k,v in S.items()}
# res = []
# for j in range(N[1]):
#     a = sys.stdin.readline().rstrip()
#     if a.isnumeric():
#         res.append(S.get(int(a)))
#     else:
#         res.append(int(T.get(a)))
# for i in res:
#     print(i)
#%%
