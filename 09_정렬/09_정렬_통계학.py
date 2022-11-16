import sys
import math
N = int(sys.stdin.readline())
a , b=[] , []
for i in range(0,8001):
    a.append(0)
    #b.append(0)
sum =0
for i in range(N):
    idx = int(sys.stdin.readline())
    if idx<0:
        a[idx+4000] +=1

    else:
        a[idx+4000] +=1
    sum+= idx
    b.append(idx)
#a[4000] => 양수
#a[-1] = a[8000] => 음수
#a[-2] = a[7999] => 음수
#a[3999] = -1일때
#최빈값 구하기
maxe = a.count(max(a))
frst =a.index(max(a))
#print("frst : {}".format(frst))
if maxe >1:
    d= a[frst+1:].index(max(a))
    d = d+frst-3999
    #print("secd d : {}".format(d))

elif maxe == 1 :
    d = frst
    d = d-4000
avg = round(sum/N)
print(avg)
e = sorted(b ,reverse=False)
#print("e : {}".format(e))
#print(math.ceil(len(b)/2))
print(e[math.ceil(len(b)/2)-1])
print(d)# 최빈값
if max(b) <0 :
    print(abs(max(b) - min(b)))
else:
    print(max(b) - min(b))
#%%
