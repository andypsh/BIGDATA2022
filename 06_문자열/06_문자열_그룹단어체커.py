import sys

N = int(sys.stdin.readline())
sum = N
for j in range(N):
    A = list(map(str, sys.stdin.readline().rstrip()))
    B = sorted(list(set(A)))
    print(A)

    res = []
    for i in B:
        count_alphabet = A.count(i)
        a = A[::].index(i)
        b = len(A) - 1- A[::-1].index(i)
        #print(a, b)
        if b-a+1 != count_alphabet:
            sum-=1
            break

print(sum)
