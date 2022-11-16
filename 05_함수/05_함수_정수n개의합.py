import sys

def solve(a : list) -> int: #주석값이다. 화살표는 a:list 이것도 주석이다.
    sum =0
    for i in a:
        sum+=i
    return print(sum)

# A = list(map(int, sys.stdin.readline().split()))
# print(solve(A))