import sys

N = int(sys.stdin.readline())

A = sorted(list(map(int , sys.stdin.readline().split(' '))))

Res = 0



for k in range(N):
    find = A[k]
    i = 0
    j = N -1
    
    while True:
        # print('A[i] : {} + A[j] {} ?? find= {}'.format(A[i] , A[j] , find) )

        if A[i] + A[j] == find :
            print('A[i] : {} + A[j] {} == find= {}'.format(A[i] , A[j] , find) )
            if i != k and j != k:
                Res +=1
                break
            elif A[i] == A[j]:
                break
            elif i ==k :
                j -= 1
        elif A[i]+ A[j] < find: #find 값보다 작을 경우 작은 값의 인덱스 증가 시킨다.
            i += 1
        elif A[i] + A[j] > find: #find 값 보다 클 경우 큰 값의 인덱스 감소 시킨다.
            j -= 1
        if i>= j:
            break
print(Res)

#%%
