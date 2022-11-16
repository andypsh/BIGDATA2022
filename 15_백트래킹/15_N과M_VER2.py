import sys

def backtracking():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i] == True:
            continue
        visited[i] = True
        s.append(i)
        backtracking()
        s.pop()
        visited[i] = False


n,m = map(int, sys.stdin.readline().split())
s = []

visited =[False for i in range(n+1)]

backtracking()
#%%
