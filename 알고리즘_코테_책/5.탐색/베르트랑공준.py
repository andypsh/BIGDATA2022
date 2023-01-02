import sys
import math
def is_prime(n , m): #n이하의 개수

    A = [True] * (m+1)

    A[0],A[1] = False , False

    for i in range(2,int(math.sqrt(m)) +1):
        if A[i] == True:
            p=2
            while i*p <= m:

                A[i*p]= False
                p+=1
    # print(A)
    A[n] = False
    sum = 0
    t = 0
    for k in range(n ,len(A)):
        if A[k] == True:
            sum+=1
    # print(len(A[n:m]))
    # print(t)
    return sum
res= []
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    else:
        # print(f'cal(2*n) : {cal(2*n) }')
        # print(f'cal(n) : {cal(n)}')
        res.append(is_prime(n , 2*n))
for k in res:
    print(k)



#%%
