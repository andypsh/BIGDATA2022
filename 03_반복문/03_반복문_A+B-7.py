import sys

T = int(sys.stdin.readline())

a=0
B =[]
while True:
    if a!=T:
        a+=1
        res = 0
        A = list(map(int, sys.stdin.readline().split()))

        res = A[0] + A[-1]
        B.append(res)
    else:
        break

for i in range(len(B)):
    print("Case #{} : {}".format(i+1, B[i])  )