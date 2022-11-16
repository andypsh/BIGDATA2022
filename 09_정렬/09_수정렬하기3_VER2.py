import sys

N = int(sys.stdin.readline())
res =[]
a=[]
for i in range(10001):
    a.append(0)
for i in range(N):
    a[int(sys.stdin.readline())] +=1
    #a[5] +=1
    #a[2] += 1

for k in range(len(a)):
    if a[k]>0: #입력이 안된거는 넘어가기
        for p in range(a[k]):
            print(k)

