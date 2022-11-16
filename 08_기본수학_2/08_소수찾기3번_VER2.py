import math
import sys
# 소수 판별 함수(에라토스테네스의 체)
def is_prime_number(m, n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array=[]
    for i in range(n+1):
        array.append(True)
    array[1] , array[0] = False
    # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며 ==> 루트 26 ==> 5.xxx ==int(5.xxxx) ==> 5 +1 = 6
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:

                array[i * j] = False
                j += 1
                #2*2 < 13:                2*2<5
                #array[4] = False         array[4] =False
                #j+=1 ==> j=3             j=3
                #2*3 < 13:
                #array[6] =False
                #j+=1 ==> j=4
                #2*4 < 13:
                #array[8] = False
                #2*5 < 10:
                #array[10] = False
                #j+=1 ==> j=5
                #2*6 < 12:
                #array[12] = False
                #j+=1 ==> j=6
                #2*7 < 14:
                #array[14] = False
                #j+=1 ==> j=7
                #array
    array2=[]
    for i in range(m, len(array)):

        if array[i] == True:
            array2.append(i)
    return array2


A = list(map(int, sys.stdin.readline().split()))
for i in is_prime_number(A[0],A[1]):
    print(i)
# A=[]
# a=0
# res =[]
# while True:
#     m = int(sys.stdin.readline())
#     if m!= 0:
#         A= is_prime_number(2*m)
#         for i in range(len(A)):
#             if A[i] < m :
#                 A[i] = 0
#                 a+=1
#         res.append(len(A)-a)
#     else:
#         break
#
# for i in res:
#     print(i)

#%%
