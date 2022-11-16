import sys

T = int(sys.stdin.readline())
res = []
for k in range(T):
    point = 0
    sum = 0
    A = list(map(str, sys.stdin.readline().rstrip()))
    for i in range(len(A)):
        if A.pop() == 'O':
            point+=1
            sum+=point
        else:
            point =0
    res.append(sum)

for p in res:
    print(p)

