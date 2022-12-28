import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

gap = list(map(int , sys.stdin.readline().split(' ')))

gap = sorted(gap , reverse= False)
prefix = [0 for i in range(N+1)]

i = 0
j = N-1
count = 0
while True:
    if gap[i] + gap[j] < M: #작으면 작은숫자의 인덱스 값 증가
        i+=1

    elif gap[i] + gap[j] > M: #크면 큰 숫자의 인덱스값 감소
        j -= 1

    elif gap[i]+ gap[j] == M:
        count+=1
        i+=1
        j-=1
    print(i , j)
    print(gap[i] , gap[j])
    if i >= j:
        break
print(count)


#%%
