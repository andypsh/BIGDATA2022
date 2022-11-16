import sys
import math

A = int(sys.stdin.readline())
def func(k):

    a = (pow(k,2) - k + 2)//2

    return a
k=1
while True:
    if func(k) <= A < func(k+1):
        break
    else:
        k+=1
if k% 2 == 1:
    bun_za = func(k) - A +k
    bun_mo = A-func(k)+1
else:
    bun_za =  A -func(k) +1
    bun_mo = func(k) - A + k

print( '{}/{}'.format(bun_za,bun_mo))

#%%