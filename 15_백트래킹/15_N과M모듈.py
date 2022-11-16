import itertools
import sys

n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m) #중복된 조합은 제외
#itertools의 permutations함수를 사용해서 풀이
#Permutations 는 배열에서 원하는 길이에 맞는 모든 조합을 구하는 함수이다.
#순열은 순서를 고려하여 뽑는 경우의 수이다.
for i in array:
    for j in i:
        print(j, end = ' ')
    print()
print('=======================')
array2 = itertools.combinations(nums,m) #중복된 조합 모두 포함


for i in array2:
    for j in i:
        print(j, end = ' ')
    print()
print('=======================')
array3 = itertools.combinations_with_replacement(nums,m)
#중복된 조합 모두 포함 , 1 1 / 2 2 등 본인의 조합도 포함하기
#중복조합 ==> 조합과는 다르게 같은 숫자를 중복하여 사용할 수 있다.
#(nums, m)
for i in array3:
    for j in i:
        print(j, end = ' ')
    print()

print('=======================')
array4 = itertools.product(nums, repeat=m)
#중복된 조합 모두 포함 , 1 1 / 2 2 등 본인의 조합도 포함하기
#중복 순열 ==> 순열과는 다르게 같은 숫자를 중복하여 사용할 수 있다.
#(nums, repeat = m)
for i in array4:
    for j in i:
        print(j, end = ' ')
    print()
#%%
