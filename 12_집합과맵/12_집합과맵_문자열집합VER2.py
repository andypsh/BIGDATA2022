# 값의 순서, index에 접근할때는 보통 list를 많이 사용하고,
# 값의 탐색이나 확인은 보통 dictionary, set형을 많이 사용한다.


import sys

N = list(map(int, sys.stdin.readline().rstrip().split()))
S=[]
M =[]
for i in range(N[0]):
    a = sys.stdin.readline().rstrip()
    S.append(a)
for j in range(N[1]):
    b = sys.stdin.readline().rstrip()
    M.append(b)
cnt = 0
for i in M:
    if i in S:
        cnt+=1
print(cnt)