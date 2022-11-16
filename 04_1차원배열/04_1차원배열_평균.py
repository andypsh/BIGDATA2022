import sys

N = int(sys.stdin.readline())

while True:
    A = list(map(int, sys.stdin.readline().split()))

    if len(A)==N :
        break

maxe = max(A)
sum , avg = 0 , 0
for i in A:
    sum+= i/maxe*100
avg = sum/N
print("%f" % avg)