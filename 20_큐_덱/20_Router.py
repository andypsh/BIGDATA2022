import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
while True:
    b = int(sys.stdin.readline())
    if b== -1:
        break
    else:

        if b==0:
            queue.popleft()
        elif len(queue) < N:
            print(queue)
            queue.append(b)
if len(queue)>0:
    # print(len(queue))
    # print(queue)
    for i in queue:
        print(i, end = ' ')
else:
    print('empty')
#%%
