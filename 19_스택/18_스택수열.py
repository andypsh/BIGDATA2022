import sys
import copy
A = int(sys.stdin.readline())
res , res2 = [] , []
basic = []
stack = []
for i in range(A):
    basic.append(i+1)
    b = int(sys.stdin.readline())
    res.append(b)
res = []
for i in res:
    for j in basic:
        if i==j:
            stack.append('pop')
        else:
            stack.append('push')




#%%
