import sys

def backtracking():
    if len(s) == m:
        # if s[1]-s[0] == 1:
        #     print('{} '.format(s[0]) *len(s))
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i] == True:
            # s.append(i)
            continue
        if visited[i-1] == True:
            s.append(i-1)
        s.append(i)
        backtracking()
        s.pop()
        visited[i] = False


n,m = map(int, sys.stdin.readline().split())
s = []

visited =[False for i in range(n+1)]

backtracking()
#%%
