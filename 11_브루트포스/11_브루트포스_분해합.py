import sys

N = int(sys.stdin.readline())
tmp = 0
for i in range(1,N+1):
    B = sum(map(int ,str(i)))
    tmp = i+B
    if tmp == N:
        print(i)
        break
    elif i == N:
        print(0)

#%%
