import sys

A = list(map(str, sys.stdin.readline().lstrip().rstrip().split()))
#split(' ')는 공백하나당 단어로 인식한다!
#따라서 split()는 공백길이와 상관없이 공백이 생기면 넘어간다.
print(len(A))

