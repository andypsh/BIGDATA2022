import sys

while True:
    T = int(sys.stdin.readline())
    res = []
    if T==-1:
        break
    else:
        for i in range(1,T):
            if T%i == 0:
                res.append(i)
        if sum(res) == T:
            print(f"{T} = " , end='')
            print(*res , sep=' + ')
        else:
            print(f"{T} is Not perfect.")
#%%
