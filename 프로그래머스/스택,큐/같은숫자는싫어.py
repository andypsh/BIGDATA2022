from collections import deque


def solution(arr):
    answer = []

    queue = deque(arr)
    queue2 = []
    # for i in range(3):
    #     print(queue[i])
    for i in range(len(arr)):
        #print(i)
        if len(queue)>1:
            print("len(queue) : {}".format(len(queue)))
            if queue[0] == queue[1]:
                queue.popleft()
                print("queue : {}".format(queue))
            else:
                queue2.append(queue.popleft())
        else:
            queue2.append(queue.popleft())
        #queue[0] == queue[1] ==> queue.popleft() ==> [1,3,3,0,1,1]
        #queue[0] != queue[1] ==> queue.append(queue.popleft()) ==> [3,3,0,1,1,1]
        #queue[0] == queue[1] ==> queue.popleft() ==> [3,0,1,1,1]
        #queue[0] != queue[1] ==> queue.append(queue.popleft()) ==> [0,1,1,1,3]
        #queue[0] != queue[1] ==> queue.append(queue.popleft()) ==> [1,1,1,3,0]
        #queue[0] == queue[1] ==> queue.popleft() ==> [3,0,1,1,1]
    #print(queue)


    # for i in arr:
    #     if i not in queue:
    #         queue.append(i)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    return queue2

solution([1,1,3,3,0,1,1])
#%%
