import sys

A= int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split(' ')))

B = sorted(B , reverse = False)
#print(B)

for i in range(len(B)-1):
    B[i+1] += B[i]

print(sum(B))


#%%
