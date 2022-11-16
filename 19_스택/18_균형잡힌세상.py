import sys
import re

A = list(map(str, sys.stdin.readline().rstrip()))
stack = []
res2= []
for i in A:
    if i in ['(' ,')','[',']']:
        stack.append(i)
idx = ""
for j in stack:
    idx +=j
# while True:
# idx = list(res.split())

# if res in '[]' or '()':
#     print(res.split('[]'))
# while True:
# print(res)
# a = re.split("[()]", res)
# print(a)
while True:
    if '()' in idx: #idx= '((())'
        B = idx.split('()') # ()를 기준으로 나눈 list 화 ['(' ,'']
        idx = ""
        for i in B: #B = ['(' , '']
            idx += i #idx = (
    if '[]' in idx: #idx= '((())'
        B = idx.split('[]]') # ()를 기준으로 나눈 list 화 ['(' ,'']
        idx = ""
        for i in B: #B = ['(' , '']
            idx += i #idx = (
    else:
        break
if idx == '':
    res2.append('YES')
else:
    res2.append('NO')
for i in res2:
    print(i)
#%%
