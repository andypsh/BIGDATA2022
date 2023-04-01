import sys

T = int(sys.stdin.readline())
A=[]
for i in range(T):
    A.append(int(sys.stdin.readline()))
# print(A)
coin =  [25 ,10 , 5 ,1]
res =[]
for k in range(T):
    cnt = [0,0,0,0]
    p=0
    for p in range(4):
        cnt[p] = A[k]//coin[p]
        A[k]-= A[k]//coin[p] * coin[p]

    res.append(cnt)

for i in res:
    print(*i)
#%%
