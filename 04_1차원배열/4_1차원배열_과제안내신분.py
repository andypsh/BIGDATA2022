import sys


dict = {key : False for key in range(1,31)}
for i in range(28):
    b = int(sys.stdin.readline())
    dict[b] =True

for i in dict.keys():
    if dict[i] == False:
        print(i)
#%%
