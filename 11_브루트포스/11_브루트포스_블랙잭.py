import sys

def BruteForce(n,p, A):
    # A=[5,6,7,13,20]
    w=0
    x=1
    y=2
    B = A[w]+A[x]+A[y]
    max = p
    res = 0
    for i in range(0,len(A)-2):
        for j in range(i+1,len(A)-1):
            for k in range(j+1, len(A)):
                B = A[i]+A[j]+A[k]

                print("{}_{}+{}_{}+{}_{} = {}".format(A[i] , i, A[j] , j , A[k] , k , B))
                # if B>p:
                #     continue
                # elif B==p:
                #     #print("{}_{}+{}_{}+{}_{} = {}".format(A[i] , i, A[j] , j , A[k] , k , B))
                #     res = B
                #     break
                if B<=p:
                    a = p-B
                    if max > a:
                        max = a
                        res = B
                        #print("{}_{}+{}_{}+{}_{} = {}".format(A[i] , i, A[j] , j , A[k] , k , B))

    return res

n = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(map(int, sys.stdin.readline().rstrip().split()))



print(BruteForce(n[0] , n[1] , C))


#%%
