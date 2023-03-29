import sys
import collections

A = list(sys.stdin.readline().rstrip().upper())
A = collections.Counter(A).most_common()
if len(A)>1:
    if A[0][1] == A[1][1] :
        print('?')
    else:
        print(A[0][0])
else:
    print(A[0][0])

#%%
