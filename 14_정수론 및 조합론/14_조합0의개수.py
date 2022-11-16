import sys


def find_two(n):
    cnt_two = 0
    while n!=0:
        n = n//2
        cnt_two +=n
    return cnt_two
def find_five(n):
    cnt_five = 0
    while n!=0:
        n= n//5
        cnt_five+=n

    return cnt_five
A = list(map(int , sys.stdin.readline().split()))
#a = find_fivetwo(fact(A[0])//(fact(A[0]-A[1])*fact(A[1])))
b = find_two(A[0])-find_two(A[1])-find_two(A[0]-A[1])
# print(find_two(A[0]))
# print(find_two(A[1]))
# c = find_five(A[0])-find_five(A[1])-find_five(A[0]-A[1])
# print('five', find_five(A[0]))
# print('five', find_five(A[1]))
d = min(find_two(A[0])-find_two(A[1])-find_two(A[0]-A[1]), find_five(A[0])-find_five(A[1])-find_five(A[0]-A[1]))
print(d)

#%%
