import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline())
B =[]
for i in range(N):
    c = list(map(str, sys.stdin.readline().rstrip().split(' ')))

    if c[0] == 'push':
        queue.append(c[1])
    elif c[0] == 'pop':
        if len(queue) == 0:
            B.append(-1)
        else:
            B.append(queue.popleft())
    elif c[0] == 'size':
        B.append(len(queue))
    elif c[0] == 'empty' :
        if len(queue) == 0:
            B.append(1)
        else:
            B.append(0)
    elif c[0] == 'front':
        if len(queue) == 0:
            B.append(-1)
        else:
            B.append(queue[0])

    elif c[0] == 'back':
        if len(queue) == 0:
            B.append(-1)
        else:
            B.append(queue[-1])
for i in B:
    print(i)
#%%
