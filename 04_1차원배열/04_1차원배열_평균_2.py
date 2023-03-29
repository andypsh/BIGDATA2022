import sys

N = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))
maxe = max(score)
avg = 0
for i in score:
    avg += i/maxe *100

print(avg/N)
#%%
