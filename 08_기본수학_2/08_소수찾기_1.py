import sys
import math
#
N = list(map(int, sys.stdin.readline().rstrip().split()))
#M = int(sys.stdin.readline())


gaet = 0
c=[]
sume = []
for i in range(N[0] , N[1]+1):
    c.append(i)
#print(c)
for k in c:

    b = (math.trunc(math.sqrt(k)))
    if k in (2,3):
        print(k)
    else:
        for j in range(2,b+1):
            #print("k는 {} j는 {}".format(k,j))
            if k % j ==0:
                break
            else:
                if j==b:
                    print(k)
                else:
                    continue
# for i in sume:
#     print(i)
#%%

#%%

#%%
