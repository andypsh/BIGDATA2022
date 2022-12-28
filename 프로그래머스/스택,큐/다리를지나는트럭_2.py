from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 0
    bridge = deque(0 for _ in range(bridge_length))
    # print(bridge)
    truck_weights = deque(truck_weights)
    while bridge:

        answer += 1
        bridge.popleft()

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                print("t: {}".format(t))
                bridge.append(t)
            else:
                bridge.append(0)


    return answer


print(solution(2, 10, [7, 4, 5, 6]), 8)
print(solution(100, 100, [10]), 101)
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)
#%%
