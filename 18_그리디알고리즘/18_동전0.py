import sys

A = list(map(int, sys.stdin.readline().split(' ')))
B=[]
for i in range(A[0]):
    b = int(sys.stdin.readline())
    B.append(b)
won = A[1]
cnt = 0
for i in range(len(B)-1,-1,-1):
    #print(B[i])
    c = won//B[i] #4200//1000 = 4 200//100 = 2
    won = won- B[i]*c #4200 - 4*1000 = 200
    cnt+= c
print(cnt)
#%%

#%%
