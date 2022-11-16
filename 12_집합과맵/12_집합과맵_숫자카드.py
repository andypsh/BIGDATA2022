import sys

# N = int(sys.stdin.readline())

C = list(map(int, sys.stdin.readline().rstrip().split()))

# M = int(sys.stdin.readline())
D = list(map(int, sys.stdin.readline().rstrip().split()))

res = [1 for i in range(20000001)]
e = list(set(D)-set(C))
print(e)
for i in range(len(e)):
    # print(e[i]+10000000)
    res[e[i]+10000000] =0
# print(res[9+10000000])
# print(res[-5+10000000])
res2 = []
for i in D:
    # res2.append(res[i+10000000])
    print(res[i+10000000], end = ' ')

#%%
