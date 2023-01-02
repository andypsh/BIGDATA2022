import sys
import collections
from collections import deque

N, L = map(int , sys.stdin.readline().rstrip().split(' '))

D_i = list(map(int , sys.stdin.readline().split(' ')))

#minimum = min(D_i)
#D_0 = A_0-3+1 ~ A_0
#D_2 = A_2-3+1 ~ A_2 ==> A_0 ~ A_2
#D_3 = A_3-3+1 ~ A_3 ==> A_1 ~ A_3
#D_4 = A_4-3+1 ~ A_4 ==> A_2 ~ A_4
#123 234 345 456 ==> S = 6 P =3 ==> S-P+1 = 4 ==> 4번 구한다.
res = deque()
#N = 5 L = 3
#D_i = 1 2 3 4 5

#D_0 = 1 ==> i-L+1 < 0
#D_1 = 1 ==> 1-3+1 = -1 A_0 ~ A_1

for i in range(N):
    # while True:
    #     if len(res)==0 or res[-1][0] <= D_i[i]:
    #         break
    #     else:
    #         res.pop()
    while res and res[-1][0] > D_i[i]:
        res.pop()
    res.append((D_i[i] , i))
    if res[0][1] <= i-L:
        res.popleft()
    print(res[0][0] , end = ' ')





#%%
