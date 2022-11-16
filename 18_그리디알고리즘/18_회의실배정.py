import sys

A = int(sys.stdin.readline())
res1 = []
for i in range(A):
    c = list(map(int, sys.stdin.readline().split()))
    res1.append(c)
# def greed(B):
#     cnt = 1
#     maxe = cnt
#     for i in range(len(B)):
#         for j in range(1 , len(B)-i):
#             #B리스트의 i열 2행값
#             a = B[i][0]
#             b = B[i][1]
#             c = B[i+j][0]
#             d = B[i+j][1]
#             cnt = 1
#             if c>=b :
#                 print('===')
#                 print(B[i] , B[i+j])
#                 cnt +=1
#                 print(cnt)
#
#                 cnt = cnt +greed(B[i+j :])
#         if i == len(B)-1:
#             return cnt
#         else:
#             print(cnt-i)
#             return cnt-(i)
res1 = sorted(res1 , reverse = False)
res2 = sorted(res1 , key = lambda x : x[1])
print("res1 : {}".format(res1))
print("res2 : {}".format(res2))
# count =0
# maxe = count
# for i,j in res1:
#     for k,p in res2:
#         if k>=j and p<=i and (i!=k and j!=p):
#             print("[{} , {}] [{}, {}]".format(i, j , k ,p))
#             count += 1
#             print("===\n{}".format(count))
#         if maxe < count:
#             maxe = count
#     count =0
# print(maxe)
last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in res2:
    if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
        conut += 1
        last = j
#i=1 j=4
#i=1>= last(0)
#count+= 1 ==> count=1
#last = j = 4
#i=3 , j=5
#
print(conut)
# for i in range(len(res1)):
#     res2.append(greed(res1[i:]))
#     print(res2)



#%%
