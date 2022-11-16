import sys
import math
# 1 ==> 1 //  1
# 2~7 ==> 2 // 6
# 8~19 ==> 3 // 12
# 20~37 ==> 4 // 18
# 38~61 ==> 5 //
# 6n
def func(i):
    a = (3*pow(i,2))-(3*i)+2

    return a
#an = 3n^2 -3n +1
N = int(sys.stdin.readline())

i =1
while True :
    if N == 1:
        print("1")
        break
    if func(i)<=N<func(i+1):
        print(i+1)
        break
    else:
        i+=1


#%%
