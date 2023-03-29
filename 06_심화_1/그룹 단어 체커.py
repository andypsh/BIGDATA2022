import sys

N = int(sys.stdin.readline())


# print(A)
# print(A.rfind('a'))
# print(A.find('a'))
# print(A.startswith('a'))
res = 0
for p in range(N):
    A = sys.stdin.readline().rstrip()
    B = list(set(A))
    res+=1
    for i in B:
        counts = A.count(i)
        if A.rfind(i) - A.find(i) +1 != counts:
            res-=1
            break

print(res)
# for i in B:
#     if A.rfind(i)

#%%
