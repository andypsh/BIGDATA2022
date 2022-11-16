import sys

res = []
for i in range(9):
    A= int(sys.stdin.readline())
    res.append(A)

b = max(res)

for i in range(9):
    if res[i] == b:
        res2= i+1
        break
print(b)
print(res2)