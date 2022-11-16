import sys

def fact(n):
    res = 1
    if n==1 or n==0:
        return 1
    else:
        for i in range(n,1, -1):
            res*=i
        return res
m = int(sys.stdin.readline())
A = list(str(fact(m)))
# print(A)
# print(len(A))
if '0' in A:
    for i in range(len(A)-1,-1,-1):
        if A[i]!='0':
            # print(i)
            print(len(A)-i-1)
            break
else:
    print(0)



#%%

#%%
