import sys
from collections import deque

A= list(map(int, sys.stdin.readline().split()))
queue = deque()
queue2 = deque()
for i in range(A[0]):
    queue.append(i+1)
res= []
while True:
    if len(queue) ==0:
        break
    else:
        for i in range(A[1]-1):
            queue.append(queue.popleft())
        res.append(queue.popleft())

print("<" , ", ".join(str(i) for i in res) , ">" , sep ='')
#print('<', end = '')
# for i in range(len(res)):
#     if i!= len(res)-1:
#         print(res[i] , end=', ')
#     else:
#         print(res[i], end='')
# print('>', end = '')




#%%
