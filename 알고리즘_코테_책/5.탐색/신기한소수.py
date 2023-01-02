import sys
import math
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())

def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number))==N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue

            if is_prime(number * 10 + i):
                DFS(number * 10 + i)
#N = 2
DFS(2)
#DFS(2) ==> number = 2 ==> len(str(number))=1 != N(2)
#is_prime(2 *10 +1) ==> False
#is_prime(2 *10 +3) == True ==> DFS(2*10 + 3) = DFS(23) ==> len(str(23)) =2 == N ==> print(23)
#is_pime(2 * 10 + 5) == False
#is_pime(2 * 10 + 7) == False
#is_pime(2 * 10 + 9) == True ==> DFS(2*10 + 9) = DFS(29) ==> len(str(29)) =2 == N ==> print(29)
DFS(3)
DFS(5)
DFS(7)
#%%
