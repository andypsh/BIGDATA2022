import sys
import math


def is_prime_num(n):
    res=[]
    array = []
    for i in range(n+1):
        array.append(True) #에라토스테네스의 체 사용위해 array에 True값 삽입
    array[0] , array[1] = 0 , 0
    for j in range(2, int(math.sqrt(n)) +1 ):
        if array[j] == True:
            k =2
            while j*k <= n:
                array[j*k] =0 #소수가 아니라면 0이라고 처리한다.
                k+=1
            res.append(j)
    return res #소수만 출력


T = int(sys.stdin.readline())
res = []
for k in range(T):
    a = int(sys.stdin.readline())

    #res_array = is_prime_num(a)


    c,d = a//2 , a//2
    while c > 0:
        if c in is_prime_num(c) and d in is_prime_num(d):
            res.append(f'{c} {d}')
            break
        else:
            c -= 1 #c를 -1
            d += 1 #d를 +1 하여 와리가리 하게 할 수 있다.
for i in res:
    print(i)
    # print(res)
    #
    # for x in res:
    #     if x*2 >=a :
    #         d = x
    #         break
    #
    # for i in range(res.index(d) , -1 , -1):
    #     #print(i)
    #     search_sosu = a - res[i]
    #     if search_sosu in res:
    #         if search_sosu > res[i]:
    #             res_fin.append(f'{res[i]} {search_sosu}')
    #         else:
    #             res_fin.append(f'{search_sosu} {res[i]}')
    #         break


#%%
