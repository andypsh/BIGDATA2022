import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
res = []
for _ in range(N):
    A = list(map(str, sys.stdin.readline().rstrip().split()))


    if A[0] == 'push_front':
        b = int(A[1])
        queue.appendleft(b)

    elif A[0] == 'push_back':
        b = int(A[1])
        queue.append(b)
    elif A[0] == 'pop_front':
        if len(queue)==0:
            res.append(-1)
        else:
            res.append(queue.popleft())
    elif A[0] == 'pop_back':
        if len(queue)==0:
            res.append(-1)
        else:
            res.append(queue.pop())
    elif A[0] == 'size':
        res.append(len(queue))
    elif A[0] == 'empty':
        if len(queue)==0:
            res.append(1)
        else:
            res.append(0)
    elif A[0] == 'front':
        if len(queue)==0:
            res.append(-1)
        else:
            res.append(queue[0])
    elif A[0] == 'back':
        if len(queue)==0:
            res.append(-1)
        else:
            res.append(queue[-1])
for i in res:
    print(i)

#%%
