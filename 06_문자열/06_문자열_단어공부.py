import sys

A = sorted(list(str(sys.stdin.readline().rstrip().upper())))

res2 = sorted(list(set(A)))
# print(res)
# print(res2)z

gaet2 = []
for i in range(len(res2)):
    gaet = A.count(res2[i])
    gaet2.append(gaet)
if gaet2.count(max(gaet2))>=2:
    print('?')
else:
    print(res2[gaet2.index(max(gaet2))])

# for i in range(len(res2)):
#     while True:
#         if res2[i] in res:
#             res.remove(res2[i])
#             gaet +=1
#
#         else:
#
#             break
#     gaet2.append(gaet)
#     gaet = 0
#
# gaet3 = gaet2.index(max(gaet2))
# print(res2[gaet3])

# R = list(map(str, sys.stdin.readline().rstrip().split()))
#
# stri = list(R[1])
#
# print(stri)