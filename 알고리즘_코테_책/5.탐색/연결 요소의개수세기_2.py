import sys

sys.setrecursionlimit(10000)

N , M  = map(int, sys.stdin.readline().split())

edge = [[] for i in range(N+1)]

visited = [False] * (N+1)
count = 0

for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
# print(edge)

def dfs(v):

    for e in edge[v]:
        if not visited[e]:
            visited[e] = True
            dfs(e)

for v in range(1, N+1):
    if not visited[v]:

        dfs(v)


        count+=1

print(count)



#%%
