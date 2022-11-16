import sys
import math
A = list(map(int, sys.stdin.readline().split()))
#print("A : {}".format(A))

def is_prime_number(n):
    array = []
    for i in range(n+1):
        array.append(True)
    #print("array_1 : {}".format(array))
    array[0] , array[1] = False, False
    for j in range(2 , int(math.sqrt(n))+1):
        #A[1] = 16
        #range(2,5)
        if array[j] == True:
            k =2
            while (j*k <= n):
                #2*2 < 16
                #array[4] =False
                #2*3 < 16
                #array[6] =False
                #.... array[16] =False

                #array[3] = True
                #array[6] =False
                #array[9] =False
                #array[12] =False
                #array[15] = False

                if array[j*k] == True:
                    array[j *k] = False
                k+=1
    return array
#print("array_2 : {}".format(array))
res = []
res_array = is_prime_number(A[1])
for i in range(A[0] , A[1]+1):
    if res_array[i] == True:
        res.append(i)
# print("res : {}".format(res))
for j in res:
    print(j)

#%%
