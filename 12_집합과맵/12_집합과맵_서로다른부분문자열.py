import sys

N = sys.stdin.readline().rstrip()

S =set()

for i in range(len(N)):
    for j in range(i, len(N)):
        temp = N[i:j+1]
        #문자열 받는거 주목
        S.add(temp)
print(len(S))
#%%
