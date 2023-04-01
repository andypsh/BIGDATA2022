import sys

N = int(sys.stdin.readline())

# 1 4  16 64 256 32*32 =
# 0 1  2  3  4  5
# 4 9(4+5) 25(4+5+16) 25*4 - 9-8 (17+17+15+15+ 57) (33+33+

import math
print(math.sqrt(1089))
#16*16

#정사각형 갯수 : 4**N

# 점의 갯수( ( [(4**N) //4) +1]*2 + ((4**N) //4) +-2]*2]

# 4**3 // (N) = 16개 ==> 17*2 + 15*2
res =0
def rect(N):
    if N==0:
        return 4
    else:
        return rect(N-1)+(math.sqrt(4**N) +1)*2 + ((math.sqrt(4**N) -2)*2)
print(rect(N))

N=1
print((math.sqrt(4**N) +1)*2 + ((math.sqrt(4**N) -2)*2))

#%%
