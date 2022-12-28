
from collections import Counter
from functools import reduce

def solution(clothes):
    # 1. 의상 종류별 Counter를 만든다.
    counter = Counter([type for clothe, type in clothes])
    print(counter)
    # 2. zip 함수를 통하여 counter 값 구할수도 있다.
    print("애스터리스크 : {}".format(*clothes))
    print("애스터리스크 with zip: {}".format(list(zip(*clothes))))
    counter_2 = Counter(list(zip(*clothes))[1])
    print(counter_2)
    # 3. 모든 종류의 count + 1을 누적하여 곱해준다
    answer = reduce(lambda acc, cur: acc*(cur+1), counter_2.values() , 1) - 1
    #acc 매개변수에는 counter_2의 value 값들 , cur 매개변수에는 1을
    #reduce 함수는 반복 가능한 객체 내 각 요소를 연산한 뒤 이전 연산 결과들과 누적해서 반환해 주는 함수이다.
    #counter_2.values()에는 ==> 2, 1 ==> 2*(1+1) + 1*(1+1) - 1 = 5
    #ex) target = [i for i in range(1,22)]
    # answer = reduce(lambda x, y : x+y , target) ==> 1+2 +3 + 4 + 5 +..... ==> 누적값 반환
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print("========")
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))

#%%
