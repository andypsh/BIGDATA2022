import sys

res = []
for i in range(10):
    A = int(sys.stdin.readline())
    a = A%42
    res.append(a)

res2 = set(res)
print(len(res2))