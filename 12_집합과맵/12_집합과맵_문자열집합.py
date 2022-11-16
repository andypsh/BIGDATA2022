import sys

N = list(map(int, sys.stdin.readline().rstrip().split()))
S=[]
M =[]
for i in range(N[0]):
    a = sys.stdin.readline().rstrip()
    S.append(a)
for j in range(N[1]):
    b = sys.stdin.readline().rstrip()
    M.append(b)
cnt = 0
for i in M:
    if i in S:
       cnt+=1
print(cnt)
