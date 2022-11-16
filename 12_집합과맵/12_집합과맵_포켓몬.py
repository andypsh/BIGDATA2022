import sys


B = {}
for i in range(5):
    B[i] = i
print(B)
#
N = list(map(int, sys.stdin.readline().rstrip().split()))
# # # #print(N)
S = {}
for i in range(N[0]):
    S[i] = sys.stdin.readline().rstrip()

T ={v:k for k,v in S.items()} #// {'AA': '0', 'BB': '1', 'CC': '2'}
# a=3
# b = 'pica'
# print(type(a))
# if type(b) == int:
#     print('good')
# else:
#     print('not good')
res = []
for j in range(N[1]):
    a = sys.stdin.readline().rstrip()
    if a.isnumeric():
        res.append(S.get(int(a)))
    else:
        res.append(T.get(a))
for i in res:
    print(i)
# a = sys.stdin.readline().rstrip()
# if a.isnumeric() :
#     print(a.isnumeric())
# else:
#     print(a.isnumeric())


#%%
