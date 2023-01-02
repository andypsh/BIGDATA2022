import sys
sys.setrecursionlimit(10000) #최대 재귀한도
N , M = map(int,sys.stdin.readline().split())

edge = [ [] for i in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)

def dfs(e):

    if not visited[e]:
        visited[e] = True
        for p in edge[e]:
            dfs(p)


count = 0
for j in range(1,N+1):

    if not visited[j]:
        dfs(j)

        count+=1
print(count)

#%%
