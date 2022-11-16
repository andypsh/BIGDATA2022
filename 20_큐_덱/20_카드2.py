import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
for i in range(N):
    queue.append(i+1)

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    else:
        queue.popleft()
        print(queue)
        queue.append(queue.popleft())
        print(queue)

#%%
