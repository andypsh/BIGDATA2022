import sys

A = str(sys.stdin.readline().rstrip())

croatia = ['c=' , 'c-' ,'dz=' ,'d-' ,'lj','nj','s=','z=']
count = 0
for i in croatia:
    if i in A:
        count += A.count(i)
print(len(A)-count)


#%%
