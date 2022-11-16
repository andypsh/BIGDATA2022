import sys
import math
#
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())


gaet = 0
c=[]
sume = []
def sosu(a):
    b = (math.trunc(math.sqrt(a)))

    if b//10 >=1:
        sosu(b)
        c.append(b)
    else:
        c.append(b)
        if b/2 >1:
            sosu(b)
        else:
            return b
for j in range(N,M+1):


    sosu(j)

    c.sort()

    if len(c)==1 and c[0]==1:
        if j==1 :
            gaet+=0

        else:
            #print("{}는 소수입니다.".format(j))
            sume.append(j)
    else:
        if c[0] ==1:
            c[0]+=1
        for i in range(c[0],c[-1]+1):
            if j%i ==0:

                break

            else:
                if i==c[-1]:
                    #print("{}는 소수입니다.".format(j))
                    sume.append(j)
    c=[]
if len(sume)>=1:
    b = sum(sume)
    print(b)
    print(sume[0])
else:
    print(-1)
#%%
