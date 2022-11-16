import sys
import math
#

A = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().rstrip().split()))
#M = int(sys.stdin.readline())


gaet = 0
c=[]
sume = []
for p in N: #[1,3,5,7]
    b = (math.trunc(math.sqrt(p)))
    #b = 1 , 1 , 2 , 2
    if p in (2,3):
        gaet+=1 #p값이 2와 3이면 갯수 1개 up
    else:
        for j in range(2,b+1):
            #print("k는 {} j는 {}".format(k,j))
            if p % j ==0: #2부터 5까지 나눠지면 0 ==> 소수가 아니다.
                break
            else:
                if j==b: #끝까지 for문 돌렸는데도 몫이 0이 안된다면
                    gaet+=1 #소수이므로 gaet +=1
                else:
                    continue
print(gaet)

#%%
