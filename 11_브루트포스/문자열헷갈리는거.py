import sys
#입력 216
N = int(sys.stdin.readline())
print(N)
#출력 : 216
print(list(map(int,str(N))))
#출력 : [2,1,6]

#입력 216
M = list(map(int ,sys.stdin.readline().rstrip()))
print(M)
#출력 : [2,1,6]

O = list(map(str, sys.stdin.readline().rstrip().split()))
print(O)
#출력 : ['216']

P = list(map(str, sys.stdin.readline().rstrip()))
print(P)
#출력 : ['2','1','6']
Q = list(map(int, sys.stdin.readline().rstrip()))
print(Q)
#출력 : [2,1,6]

#입력 : 216 215
R = list(map(int, sys.stdin.readline().rstrip().split()))
print(R)
#출력 : [216,215]

print(str(365)[0] + str(365)[1])
#출력 36

#%%
