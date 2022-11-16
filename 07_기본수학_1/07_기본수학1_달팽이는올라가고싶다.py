import sys

#A = list(map(int, sys.stdin.readline().rstrip().split()))
#print(A)

# a = A[0]
# b = A[1]
# V = A[2]
# for i in range(3):
A = list(map(int, sys.stdin.readline().rstrip().split()))
a = A[0]
b = A[1]
V = A[2]
def func(k , a, b):
    res = (a-b)*k + b
    return res
k = (V-b)//(a-b)
if func(k ,a ,b) < V < func(k+1, a, b):
    print(k+1)

elif func(k,a,b) == V:
    print(k)