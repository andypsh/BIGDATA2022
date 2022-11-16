import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())



gaet = 0
c=[]
sume = []
for p in range(M,N+1): #자연수 M부터 N까지 FOR문으로 돌린다.


    b = (math.trunc(math.sqrt(p)))
    if p in (2,3):
        c.append(p)
    else:
        for j in range(2,b+1):

            if p % j ==0: #나눠지는게 있으면 소수가 아니다.
                break
            else:
                if j==b: #나눠지는게 for문의 끝까지갔을때 없으면 소수이므로
                    c.append(p) #c리스트에 추가한다.
                else:
                    continue
if len(c)>=1: #c리스트에 소수가 없을수 있으므로 1개 이상이 있을경우
    print(sum(c)) #c리스트내 전체값 더한값
    print(c[0]) #처음 c값을 출력한다.
else: #c리스트가 0개인 경우
    print(-1) #-1을 출력한다.

#%%
