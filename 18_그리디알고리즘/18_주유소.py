import sys

a = int(sys.stdin.readline())

b = list(map(int ,sys.stdin.readline().split()))

c = list(map(int, sys.stdin.readline().split()))

price = c[0]*b[0] #초기값
idx = c[0]
#print(idx)
for i in range(1, len(c)-1):
    #print(c[i])
    if c[i] < idx:
        # print("idx : {}".format(idx))
        idx = c[i]
        price += idx*b[i]
    else:
        price += idx*b[i]
print(price)

# for i in range(1, len(c)-1):
#     print(b[i])
#%%
