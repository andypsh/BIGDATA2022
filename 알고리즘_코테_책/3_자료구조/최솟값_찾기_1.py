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

#N = 5 L = 3
#D_i = 1 2 3 4 5

#D_0 = 1 ==> i-L+1 < 0
#D_1 = 1 ==> 1-3+1 = -1 A_0 ~ A_1
end_idx = 0
for i in range(N):
    idx = end_idx-L+1
    if end_idx == 0 or idx<=0:
        print(min(D_i[0:end_idx+1]) , end = ' ')
        end_idx+=1
    else:
        print(min(D_i[idx: end_idx+1]) , end = ' ')
        end_idx+=1





#%%
