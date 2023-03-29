import sys

C = int(sys.stdin.readline())
res = []
for p in range(C):
    score = list(map(int , sys.stdin.readline().split()))
    counts = score[0]
    score = score[1:]
    avg = (sum(score) / counts)
    score = list(filter(lambda x : x>avg ,score))
    res.append(round(len(score)/counts *100 , 3))
for i in res:
    print("%.3f" %i + "%")

#%%
