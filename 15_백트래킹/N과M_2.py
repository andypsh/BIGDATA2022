import sys

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    #조건으로 위에 설명한 방문했을 때는 제외시키도록 조건문을 걸어주어 아직 방문하지 않은 경우에만 방문
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        print(s)
        print(visited)
        visited[i] = False


n, m = map(int, sys.stdin.readline().split())
s = []
visited = [False] * (n+1)

dfs()
#%%
