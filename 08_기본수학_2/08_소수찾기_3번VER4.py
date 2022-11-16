import sys
import math
#에스토스테너스의 체 연습

N = list(map(int, sys.stdin.readline().rstrip().split()))



def is_prime_number(n):
    array = [True for i in range(n+1)]
    array[0] , array[1] = False, False
    for j in range(2 , int(math.sqrt(n))+1):
        if array[j] == True:
            k =2
            while (j*k <= n):
                if array[j*k] == True:
                    array[j *k] = False
                k+=1
    return array
res = []
res_array = is_prime_number(N[1])
for i in range(N[0] , N[1]+1):
    if res_array[i] == True:
        res.append(i)
# print("res : {}".format(res))
for j in res:
    print(j)





#%%
