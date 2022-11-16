import sys

def bubble_sort(A):
    n = len(A)
    for i in range(n-1 , 0 , -1):
        bChanged = False
        for j in range(i):
            if (A[j] > A[j+1]) :
                A[j] , A[j+1] = A[j+1] , A[j]
                bChanged = True


        if not bChanged: break;
    return A

N = int(sys.stdin.readline())
B =[]
for i in range(N):
    A = int(sys.stdin.readline())
    B.append(A)
C = bubble_sort(B)
for i in C:
    print(i)