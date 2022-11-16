import sys

C = int(sys.stdin.readline())
res = []
for i in range(C):
    A = list(map(int,sys.stdin.readline().split()))
    avg = 0
    sum =0
    for j in range(1,A[0]+1):
        sum+= A[j]
    avg = sum/A[0]
    a = 0
    for p in A[1:]:

        if p>avg:
            a+=1
    res.append(round(a/A[0]*100,3))


for k in res:
    print("%.3f" %k + "%")
# import sys
#
# C = int(sys.stdin.readline())
# res = []
# for i in range(C):
#     A = list(map(int,sys.stdin.readline().split()))
#     avg = 0
#     for j in range(1,A[0]+1):
#         avg+= A[j]/A[0]
#     a = 0
#     for p in A[1:]:
#
#         if p>avg:
#             a+=1
#     res.append(round(a/A[0]*100,3))
# for k in res:
#     print("%.3f" %k + "%")
# A = list(map(int,sys.stdin.readline().split()))
# for p in A[1:] :
#     print(p)
#
# for i in range(1,7):
#     print(i)
# num = int(input())
#
# for _ in range(num):
#     scores = list(map(int, input().split()))
#     avg = sum(scores[1:])/scores[0]
#
#     cnt = 0
#     for i in scores[1:]:
#         if i > avg:
#             cnt += 1
#
#     per = (cnt/scores[0])*100
#     print('%.3f' %per + '%')
# import sys
# C = int(input())
#
# for i in range(C):
#     Score = list(map(int, input().split()))
#     Mean = sum(Score[1:])/Score[0]
#     cnt = 0
#     for j in range(1, len(Score)):
#         if Score[j] > Mean:
#             cnt += 1
#     percent = 100*cnt/Score[0]
#     print("{:.3f}%".format(round(percent,3)))
#%%
