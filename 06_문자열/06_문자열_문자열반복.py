import sys

T = int(sys.stdin.readline())
res=[]
for k in range(T):
    R = list(map(str, sys.stdin.readline().rstrip().split()))

    stri = list(R[1])

    idx = ''
    for i in stri:
        a = i*int(R[0])
        idx += a
    res.append(idx)
for p in res:
    print(p)