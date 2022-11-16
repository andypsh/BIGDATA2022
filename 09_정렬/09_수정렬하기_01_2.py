import sys
from collections import deque

N = int(sys.stdin.readline())
b = deque()
for i in range(N):
    a = int(sys.stdin.readline())
    b.append(a)
for j in b:
