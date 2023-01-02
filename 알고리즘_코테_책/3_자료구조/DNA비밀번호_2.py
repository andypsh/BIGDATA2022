import sys
from collections import Counter

S, P = map(int , sys.stdin.readline().split(' '))
DNA = list(map(str, sys.stdin.readline().rstrip()))
find = dict(zip(['A' , 'C' ,'G' , 'T'] ,list(map(int, sys.stdin.readline().split(' ')))))
res = 0
start_idx , end_idx = 0 ,0
base = {'A' : 0 , 'C' : 0 , 'G' : 0 , 'T' : 0}
for start_idx in range(S-P+1): #3번 , 9 8 이라면 , 9-8+1 = 2번 ,

    flag = True


    if start_idx == 0:
        for idx in range(P):
            base[DNA[idx]]+=1 #start_idx가 0 , 시작 지점일때 , 잘리는 곳 까지 +1 시킨다.
    else:
        base[DNA[start_idx + P - 1]] +=1 #start_idx가 1~ 일경우 DNA 리스트의 있는 맨끝자리만 +=1 시켜줘야한다.
        base[DNA[start_idx-1]] -=1 #start_idx 의 0부분 과 같이 이전 부분은 자른다.

    for t in list(find.keys()):
        if base[t] < find[t]:
            flag = False

            break
    if flag:
        res+=1
print(res)
#%%
