import sys

k = int(sys.stdin.readline())
b= []
for i in range(k):
    c = int(sys.stdin.readline())
    if c==0 and len(b)>=1:
        b.pop()
    else:
        b.append(c)
print(sum(b))

#%%
