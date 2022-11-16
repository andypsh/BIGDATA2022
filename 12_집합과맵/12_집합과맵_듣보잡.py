import sys

N = list(map(int , sys.stdin.readline().rstrip().split()))

S= {}

for i in range(N[0]):
    S[i] = sys.stdin.readline().rstrip()
#S = {0 : "a" ,1 : "b" , 2 : "c"}
#print(S)
cnt = 0
res = []
T = {k:v for v,k in S.items()}
# T = {"a" : 0 , "b" : 1 , "c" : 2}
for i in range(N[1]):
    a = sys.stdin.readline().rstrip()
    if T.get(a) is not None: #듣보잡 명단에 포함되어 있다면
        cnt+=1
        res.append(S.get(T.get(a)))
print(cnt)
res.sort()
for i in res:
    print(i)

#%%
