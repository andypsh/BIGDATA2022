import sys
import math

N = int(sys.stdin.readline())

T = list(map(int ,sys.stdin.readline().split()))

def is_prime( m): #n이하의 개수
    A = [True] * (m+1)
    A[0],A[1] = False , False
    for i in range(2,int(math.sqrt(m)) +1):
        if A[i] == True:
            p=2
            while i*p <= m: # 배수들 False 만들기
                A[i*p]= False
                p+=1
    return A
res=0
for i in T:
    if is_prime(i)[i]==True:
        res+=1
print(res)

#%%
