import sys

N = int(sys.stdin.readline())
B =[]
for i in range(N):
    N = int(sys.stdin.readline())
    B.append(N)

c = sorted(B)
for i in c:
    print(i)

