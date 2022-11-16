import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())


a=0
res = 0
while True:

    if a < N:
        A = list(map(int, sys.stdin.readline().split()))
        res += A[0]*A[1]
        a+=1
        #print(res)
    else:
        break

if res == X:
    print('Yes')
else:
    print('No')

#print(res)