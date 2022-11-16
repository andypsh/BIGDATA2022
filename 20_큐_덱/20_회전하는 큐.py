import sys
from collections import deque
import copy
A = list(map(int ,sys.stdin.readline().split()))
queue = deque()
for i in range(A[0]):
    queue.append(i+1)

B = list(map(int ,sys.stdin.readline().split()))
C = deque(copy.deepcopy(B))
res = []
cnt = 0
while True:
    if len(C) == 0:
        break
    else:
        if queue[0] == C[0]:
            C.popleft()
            queue.popleft()
        else:
            if len(queue)-queue.index(C[0]) >= queue.index(C[0]):
                queue.append(queue.popleft())
                cnt+=1
            else:
                queue.appendleft(queue.pop())
                cnt+=1
print(cnt)
#%%
