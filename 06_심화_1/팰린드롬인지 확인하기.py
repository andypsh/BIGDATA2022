# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 동일한 단어
import sys

A = list(sys.stdin.readline().rstrip())
if A[::1] == A[::-1]:
    print(1)
else:
    print(0)

#%%
