import sys
import math

M , N = map(int, sys.stdin.readline().split())




def is_prime_number(N):
    A = [True] * (N+1)
    A[1] , A[0] = False , False
    for i in range(2, int(math.sqrt(N))+1):

        if A[i] == True:
            k =2
            while (i*k <= N):

                if A[i*k] == True:
                    A[i*k] = False
                k+=1
    return A
res = []
res_array = is_prime_number(N)
for i in range(M , N+1):
    if res_array[i] == True:
        res.append(i)
# print("res : {}".format(res))
for j in res:
    print(j)

#%%
