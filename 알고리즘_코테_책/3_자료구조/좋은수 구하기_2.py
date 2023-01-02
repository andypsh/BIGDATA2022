import sys

N = int(sys.stdin.readline())

A = sorted(list(map(int , sys.stdin.readline().split(' '))))

Res = 0



for k in range(N):
    find = A[k]
    i_index = 0
    j_index = N -1
    # if A[i] != A[j]:
    while True:
        if A[i_index] + A[j_index] == find :

            if i_index != k and j_index != k: #자기 자신을 포함하지 않는?
                Res +=1
                print(f"i_index : {i_index}")
                print(f"j_index : {j_index}")
                print('A[i_index] : {} + A[j] {} == find= {}'.format(A[i_index] , A[j_index] , find) )
                print(f"k : {k}")
                break
            elif j_index==k:
                j_index -= 1
            elif i_index==k:
                i_index += 1
        elif A[i_index]+ A[j_index] < find: #find 값보다 작을 경우 작은 값의 인덱스 증가 시킨다.
            i_index += 1
        elif A[i_index] + A[j_index] > find: #find 값 보다 클 경우 큰 값의 인덱스 감소 시킨다.
            j_index -= 1
        if i_index>= j_index:
            break
print(Res)


#%%
