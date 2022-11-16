import sys
import re

A = str(sys.stdin.readline().rstrip()) #str 타입으로 A변수에 받아온다.
c = 0
d = 0
B = A.split('-') #B리스트에 A를 슬라이싱한다. ==> -를 기준으로 나눈다
#print(bool(A.split('-')))
# print(re.split("[-, +]" , A)) #정규식 활용시 -,+ 두개의 SPLIT()으로 나눌 수 있다.

C = B[0].split('+')
C = list(map(int, C)) #데이터 타입 변환!
c +=sum(C)
if len(B)>1:
    for i in B[1:]:
        D = i.split('+')
        D = list(map(int, D))
        d+= sum(D)
print(c - d)
# else:
#     d = 0
#     B = A.split('+')
#     #print(B)
#     B = list(map(int, B))
#     d+= sum(B)
#     print(d)





# sume = sum(B[1:])
#
# print(B[0] - sume)
# print(A.split('+'))


#55-50+40+55-50+40-55-50+40
#%%
