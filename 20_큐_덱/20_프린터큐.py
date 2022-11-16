import sys
from collections import deque

#T = int(sys.stdin.readline())
queue = deque()
A = list(map(int ,sys.stdin.readline().split()))
B = deque(map(list, sys.stdin.readline().split()))
res = []
cnt = 0
maxe = max(B)
while True:

    if maxe == B.popleft():
        cnt+=1
        break
    else:
       B.append(B.popleft())
       cnt+=1
print(B)
print(cnt)
# B = list(map(int, sys.stdin.readline().split()))
# S = {}
# C = []
# for i in range(A[0]):
#     S[i] = B[i]
# print(S)
#
# for i in S.keys():
#     j = S[i]
#     C.append([i,j])
# for i in S:
#     for j in i:
#         maxe
# print(C)

# for i in range(len(C)):
#     if C[i][0] == A[1]:
#         print(i)
#         break





# print(S)
# C = sorted(C , key = lambda x : x[1] , reverse=True)
# print(C)
# d = C[::][1].index(A[1])
# print(d)
# C = list(B)
# print(B)
# print(C)
# B = deque(map(int , B))
# for i in range(len(B)):
#     B[i].append(i)
# B = sorted(B, reverse=True)
# print(B)
# print(A.index(6))
# print(B[:][1].index(1))
# maxe = A[0]
# while True:
#     if deque[0] == A[1]:
#         break
#     elif


#%%
