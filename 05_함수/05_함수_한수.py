import sys

N = int(sys.stdin.readline())
A =[]
res = 0
for i in range(1,N+1):
    A.append(i)
for j in range(len(A)):
    b= list(str(A[j]))
    if len(b)>=3:
        deung = []
        b = list(map(int, b))
        for k in range(len(b)-1):
            deung.append(b[k] - b[k+1])
        if len(set(deung))==1:
            res+=1
    else:
        res+=1
print(res)