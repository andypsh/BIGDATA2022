import sys

A = int(sys.stdin.readline())

while True:
    N = list(map(int, sys.stdin.readline().rstrip()))
    if len(N) == A:
        break
sum = 0
for i in N:
    sum+=i

print(sum)