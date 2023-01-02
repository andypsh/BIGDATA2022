import sys
sys.setrecursionlimit(10000)



N, M = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
#N = 6 , M = 5
#adj(EDGE) = [ [] [] [] [] [] [] [] ]
visited = [False] * (N + 1)
#visted = [ False , False , False , False , False , False , False]
count = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    adj[u].append(v)

    adj[v].append(u)
    #u , v = 1 , 2
    #adj[1].append(2) ==> adj = [ [] [2] [] [] [] [] [] ]
    #adj[2].append(1) ==> adj = [ [] [2] [1] [] [] [] [] ]

    #u , v = 2 , 5
    #adj[2].append(5) ==> adj = [ [] [2] [1,5] [] [] [] [] ]
    #adj[5].append(2) ==> adj = [ [] [2] [1,5] [] [] [2] [] ]

    #u , v = 5 , 1
    #adj[5].append(1) ==> adj = [ [] [2] [1,5] [] [] [2,1] [] ]
    #adj[1].append(5) ==> adj = [ [] [2,5] [1,5] [] [] [2,1] [] ]

    #u , v = 3 , 4
    #adj[3].append(4) ==> adj = [ [] [2,5] [1,5] [4] [] [2,1] [] ]
    #adj[4].append(3) ==> adj = [ [] [2,5] [1,5] [4] [3] [2,1] [] ]

    #u , v = 4 , 6
    #adj[4].append(6) ==> adj = [ [] [2,5] [1,5] [4] [3,6] [2,1] [] ]
    #adj[6].append(4) ==> adj = [ [] [2,5] [1,5] [4] [3,6] [2,1] [4] ]
for e in adj[4]:
    #adj = [ [] [2,5] [1,5] [4] [3,6] [2,1] [4] ]
    print(e) #e = 3 , 6
    if not visited[e]:
        print(visited[e])
    else:
        print('no')
def dfs(v):
    visited[v] = True
    for e in adj[v]:
        #adj = [ [] [2,5] [1,5] [4] [3,6] [2,1] [4] ]

        if not visited[e]:
            dfs(e)
# #visited = [ False , False , False , False , False , False , False]
#
for j in range(1, N + 1):
    if not visited[j]: #visited 가 False일때 , visited = [False , True , True , False,
        dfs(j)

        #j = 1
        #dfs(1)
        #visited[1] = True
        # for e in adj[1]=[2,5] , e= 2 , 5

        #visited[2] = False ==> dfs(2) , visited[5] = False ==> dfs(5)
        #dfs(2)
        #visited[2] = True
        #for e in adj[2] = [1,5] , e = 1 , 5

        #if not visited[1]= True'''' visited[5] = False
        #dfs(5)
        #visited[5] =True
        #for e in adj[5] = [2 , 1] , e = 2 , 1:

        #if not visited[2] = True , visited[1] = True


        #visited = [False , True , True , False, False , True , False]

        #count+= 1


        #j = 2
        #visited[2] = True

        #j = 3

        #visited[3] = False

        #dfs(3)
        #visited[3] = True
        #for e in adj[3] = [4]

        #if not visited[4] = False

        #dfs(4)
        #visited[4] = True
        #for e in adj[4] = [3,6] , e= 3 ,6

        #if not visited[3] = True , visited[6] = False
        #dfs(6)
        #visited[6] =True
        #for e in adj[6] = 4

        #if not visited[4] = True

        #visited = [False , True , True, True , True, True, True]
        #count+=1 = 2

        #j = 4

        #visited[4] = True

        #j=5

        #visited[5] = True

        #j=6

        #visited[6] = True

        count += 1

print(count) # count = 2

#%%
