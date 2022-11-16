import sys
import collections
import itertools

def solution(nums):
    b = len(nums)
    hashes = collections.Counter(nums)
    #answer = itertools.product(nums, repeat=2)
    answer2 = []
    #for i in answer:
    #   print(i)
    answer = len(hashes.keys())
    if answer > b//2:
        answer = b//2
    return answer

nums = list(map(int, sys.stdin.readline().split()))

print(solution(nums))

#%%
