import sys

N = int(sys.stdin.readline())

while True:
    A = list(map(int, sys.stdin.readline().split()))

    if len(A)>N:
        print("다시입력하세요")

    else:
        break

print(min(A) , max(A))

