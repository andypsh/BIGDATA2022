import sys
from collections import deque
# res = []

T = int(sys.stdin.readline())
for _ in range(T):
    array = list((sys.stdin.readline().rstrip()))
    #print(array)
    flag = 0
    n = int(sys.stdin.readline())
    queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    # print(queue)
    if n==0:
        queue = deque()
    for i in range(len(array)):
        if array[i]== 'R' :
            flag+=1
            # a = list(queue)
            # queue = deque(a[::-1])
            # print(queue)
        elif array[i] =='D':
            if len(queue)>=1:
                if flag%2==0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                break
                #res.append('error')
    else:
        # res2= []
        if flag % 2 ==1:
            # a = list(queue)
            # queue = deque(a[::-1])
            queue.reverse()
            print("[" + ",".join(queue) + "]")
            # queue = list(map(int,queue))
            # for i in queue:
            #     res2.append(",".join(i))
            # res.append(res2)
        else:
            #queue = list(map(int,queue))
            print("[" + ",".join(queue) + "]")
            #res.append(res2)
# for i in res:
#     print(i)



#%%
