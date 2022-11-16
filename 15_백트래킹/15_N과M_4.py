# import sys
#
# import sys
#
# def dfs(start):
#     if len(s) == m:
#         print(' '.join(map(str , s)))
#         return
#     for i in range(start, n+1):
#
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs(i+1)
#         s.pop()
#         visited[i] = False
#
# n,m = map(int , sys.stdin.readline().split())
#
# s = []
#
# visited = [False for i in range(n+1)]
# dfs(1)
# import sys
#
# def backtracking():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, n+1):
#         if visited[i] == True:
#             continue
#         if visited[i-1] == True:
#             s.append(i-1)
#             continue
#         s.append(i)
#         backtracking()
#         s.pop()
#         visited[i] = False
#
#
# n,m = map(int, sys.stdin.readline().split())
# s = []
#
# visited =[False for i in range(n+1)]
# backtracking()
import itertools
import sys

n,m = map(int , sys.stdin.readline().split())
res = [i for i in range(1, n+1)]

array = itertools.combinations_with_replacement(res , m)
for i in array:
    for j in i:
        print(j, end =' ')
    print()

#%%
