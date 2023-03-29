import sys

maxe = 0
for i in range(9):
    a = int(sys.stdin.readline())
    if maxe < a:
        maxe = a
        indexe = i+1


print(maxe)
print(indexe)
#%%
