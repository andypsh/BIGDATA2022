import sys

while True :
    a = list(map(int, sys.stdin.readline().split()))
    #print(set(a))
    if len(a) ==3:
        break
    else:
        print("주사위는 3번만 굴려!")
# if a & b & c == True
a.sort(reverse=True)
#print(a)
b = list(set(a))
b.sort(reverse=True)
# # print(b)
cnt = 0
res = 0
if len(b) == 3:
    print(max(b) *100)
elif len(b)==2:

    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] == a[j]:
                cnt+=1
        if cnt ==2 :
            res = b[i]
        else:
            cnt=0
    print(a)
    print(b)
    print(1000 + res*100)
else:
    print(10000+a[0]*1000)
# print("겹치는 개수" , cnt)

#%%
