import sys
N, M = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# DP 활용한 파스칼삼각형 풀기
# nCk = (n-1)C(k-1) + (n-1)Ck
# 파스칼 삼각형 선언
pascal = [0]
for dp in range(2, N+2):
     pascal.append([0]*dp)
print(pascal)
# # pascal[i] = [1, ?, ?, ..., ?, 1]에서 i는 nCk에서 n, 리스트의 인덱스는 k를 의미

pascal[1] = [1, 1]
for dp in range(2, N):
    pascal[dp][0] = 1
    for idx in range(1, dp):
        pascal[dp][idx] = (pascal[dp-1][idx-1] + pascal[dp-1][idx]) % 10007
    pascal[dp][-1] = 1
print(pascal)

if M == 0 or M == N:
    print(1)
else:
    print((pascal[N-1][M-1] + pascal[N-1][M]) % 10007)
#%%
