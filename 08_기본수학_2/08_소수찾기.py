import sys
import math
#
N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

#소수
#2 3 5 7 11 13 17 19 23 29 31
#루트 1 = 1 루트 2 = 1.xx 루트 3 = 1.xxx => 3개(2개)
#루트 4 = 2 루트 5 = 2.xxxx 루트 6 =2.xxx 루트 7 =2.xxx 루트 8 =2.xxx =>5개(2개)
#루트 9 = 3 ~~~~~~~~~~~~~~~~~~~~~~~~~루트 15 = 3.xxx => 7개(2개)
#루트 16 = 4 ~~~~~~~~~~~~~~~~~~~~~~~ 루트 24 = 4.xxx =>9개(3개)
#루트 25 = 5 ~~~~~~~~~~~~~~~~~~~~~루트 35 = 5.xxxx => 11개(2개)
#소수 판별 : 2 3
gaet = 0
c=[]
def sosu(a):
    b = (math.trunc(math.sqrt(a)))

    if b//10 >=1:
        sosu(b)
        c.append(b)
    else:
        c.append(b)
        if b/2 >1:
            sosu(b)
        else:
            return b
# sosu(1025)
# c.sort()
# print(c)
#
# if c[0] == 1:
#     if c[0]==1 :
#         print("소수가아닙니다.")
#
#     else:
#         #print("소수입니다.")
#         gaet+=1
# else:
#     for i in range(c[0],c[-1]+1):
#         if 1025%i ==0:
#             #print("소수가아닙니다.")
#             break
#
#         else:
#             if i==c[-1]:
#                 #print("소수입니다.")
#                 gaet+=1
# print(gaet)
for j in A:


    sosu(j)

    c.sort()
    #print(c)
    if len(c)==1 and c[0]==1:
        if j==1 :
            gaet+=0

        else:
            #print("{}는 소수입니다.".format(j))
            gaet+=1
    else:
        if c[0] ==1:
            c[0]+=1
        for i in range(c[0],c[-1]+1):
            if j%i ==0:
                #print("{}소수가아닙니다.".format(i))
                break

            else:
                if i==c[-1]:
                    #print("{}는 소수입니다.".format(j))
                    gaet+=1
    c=[]
print(gaet)
# sosu(3)
#
# c.sort()
# print(c)

#%%
