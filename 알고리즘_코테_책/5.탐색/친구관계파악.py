import sys

sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

edge = [[] for i in range(N)]

visited = [False] * (N)

for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
# print(edge)
arrive = False
def DFS(p):
    for e in edge[p]:
        if not visited[e]:
            visited[e]= True

            DFS(e)
# DFS(0)

def dfs(start , depth):
    global arrive
    visited[start]=True
    if depth==5:
        arrive = True
        return
    for i in edge[start]:
        if visited[i] == False:
            dfs(i , depth+1)
    visited[start]=False
for i in range(N):
    dfs(i ,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
# DFS(0)
# e = edge[0] = 4
#visited[4] = False ==> visited[4] = True

#DFS(4)
#e = edge[4] = 7 , 3 , 6 , 0
#visited[7] = False ==> visited[7] = True

#DFS(7)
#e = edge[7] = 1 , 3, 4 ,2
#visited[1] = False ==> visited[1] = True//// visited[3] = False ==> visited[3] = True //// visited[4] = True


#DFS(1) //// DFS(3)
#e = edge[1] = 7 //// e = edge[3] = 7,4,5
#visited[7] = True ////visited[7] = True //// visited[4] = True //// visited[5] = False ==> visited[5] =True

#DFS(5)
#e = edge[5] = 3
#visited[3] = True

#%%
