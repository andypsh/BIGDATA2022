import sys

N = int(sys.stdin.readline())

for i in range(N-1,-1,-1):
    A = " " * i
    B = "*" * (N-i)
    # print(i)
    # print(N-i)
    print(A+B)

print("*"*5)

#%%
