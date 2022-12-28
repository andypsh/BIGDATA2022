import sys

M = list(map(int , sys.stdin.readline().split(' ')))

A = [[0] * (M[0]+1)]
D = [[0] * (M[0]+1) for _ in range(M[0]+1)]

for i in range(M[0]):
    A_row = [0] + [int(x) for x in sys.stdin.readline().split()]
    A.append(A_row)

for i in range(1,M[0]+1):
    for j in range(1 , M[0]+1):

        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
print(D)
for _ in range(M[1]):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

    print(result)
#%%
