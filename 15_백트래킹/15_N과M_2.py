import sys

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str , s)))
        return
        # a = (' '.join(map(str, s)))
        # return res.append(s)
    # if len(s) ==0:
    #     b = 1
    # else:
    #     b = s[0]
    for i in range(start, n+1):

        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i+1)
        s.pop()
        #print(s)
        #print(visited)
        visited[i] = False

n,m = map(int , sys.stdin.readline().split())

s = []

visited = [False for i in range(n+1)]
res = []
# b= 1
idx = []
#dfs()
#print(res)
dfs(1)
# for i in dfs():
#     print(i)

#%%
