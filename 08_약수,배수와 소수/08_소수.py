import sys
import math

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

def is_prime(m):

    arr = [True] * (m+1)

    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(m))+1) :
        if arr[i] == True:
            p=2
            while i*p <= m: # 배수들 False 만들기
                arr[i*p]= False
                p+=1
    A = list(filter(lambda x : arr[x] == True  , range(len(arr))))
    return A
A = list(filter(lambda x: x>=M ,is_prime(N)))
if A:
    print(sum(A))
    print(min(A))
else:
    print(-1)




#%%
