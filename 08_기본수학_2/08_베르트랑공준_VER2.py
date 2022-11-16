import math
import sys

def is_prime_number(m, n):
    array=[]
    for i in range(n+1):
        array.append(True)
    array[1] , array[0] = False ,False
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:

                array[i * j] = False
                j += 1
    array[m] = False
    array2=[]
    sum = 0
    for i in range(m, len(array)):

        if array[i] == True:
            sum+=1
    return sum
res=[]
while True:
    A = int(sys.stdin.readline())
    if A != 0:
        res.append(is_prime_number(A, 2*A))

    else:
        break
for i in res:
    print(i)
