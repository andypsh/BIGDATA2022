import sys
import collections

hashDict = {}
sumHash = 0
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion  = 	["josipa", "filipa", "marina", "nikola"]
#HashMap이란 Key-Value의 Pair를 관리하는 클래스이다.
#Key는 hash한 값이 되겠고, Value는 각 선수의 이름으로 해둔다.
# for part in participant:
#     hashDict[hash(part)] = part
#     print("hashDict : {}".format(hashDict))
#     sumHash += hash(part)
#     print("sumHash : {}".format(sumHash))
#
# for comp in completion:
#     sumHash -= hash(comp) #hash의 key 값 제거한다.
#
# print(hashDict[sumHash])
a = collections.Counter(participant)
b = collections.Counter(completion)
print(a)
print(b)

print(a-b)
answer = a-b
print(list(answer.keys())[0])

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
# solution(participant, completion)
#%%
