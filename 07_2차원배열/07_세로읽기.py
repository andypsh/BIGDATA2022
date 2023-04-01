import sys

A= []
maxe = 0
for i in range(5):
    a = list(sys.stdin.readline().rstrip())
    idx = len(a)
    if idx > maxe:
        maxe = idx
    A.append(a)
for k in range(maxe):
    p=0
    while True:
        if p==5:
            break
        try:
            print(A[p][k] , sep='' , end='')
            p+=1
        except IndexError:
            p+=1
# print(A)
#%%
