import sys

A = list(map(str , sys.stdin.readline().rstrip().split()))
# print(A)
B = list(A[0])
C = list(A[1])

D = B[::-1]
E = C[::-1]
str ,str2= "" , ""
for i in D:
    str+=i
for i in E:
    str2+=i
print(max(str, str2))
# print(str)