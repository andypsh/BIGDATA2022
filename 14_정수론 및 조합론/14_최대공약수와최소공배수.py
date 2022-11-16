import sys

A= list(map(int,sys.stdin.readline().rstrip().split()))
A= sorted(A , reverse=True)
seo, dae = 0,0

#유클리드 호제법
#큰 수를 작은 수로 나눈 나머지를 구한다.
#그다음 나눴던 수와 나머지로 또 mod연산을 진행한다.
#나머지가 0이 됐을때 나눈 값이 최대공약수
res=0
if A[0]%A[1] ==0:
    seo = A[1]
    dae = A[0]
else:
    a,b = A[0],A[1]
    while True:
        temp = a%b
        if temp !=0:
            a = b
            b= temp

        # elif temp == 1:
        #     seo = A[1]
        #     break
        elif temp == 0:
            seo = b
            break
    dae = A[0]*A[1]//seo
print(seo)
print(dae)
#%%
