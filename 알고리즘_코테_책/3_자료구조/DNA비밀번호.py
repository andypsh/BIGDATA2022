import sys
import itertools
from collections import Counter
#ACKA는 DNA 문자열이 아니지만 "ACCA"는 DNA 문자열이다
#DNA 문자열은 "A , 'C' , 'G' ,'T' 가 포함된 문자열
#==> 투포인터 알고리즘을 사용하자

#==>AAACCTGCCAA 이고 부분문자열의 길이를 4라고 하자. 'A'는 1개이상 'C는 1개이상 ,'G는 1개이상
# 'T'는 0개 이상이 등장해야 비밀번호로 사용

#ACCT 는 G가 0개 여서 사용 불가
#GCCA는 모든 조건을 만족하기 때문에 사용 가능


S, P = map(int , sys.stdin.readline().split(' '))
print(S , P)
DNA = list(map(str, sys.stdin.readline().rstrip()))
print(DNA)
find2= list(map(int, sys.stdin.readline().split(' ')))
find = list(zip(['A' , 'G' ,'C' , 'T'] ,find2))
print("FIND : " , find)

find3 = dict(find) #zip 함수 꺼 그대로 사용
print("DIC FIND : " , find3)
res = 0
for i in range(S):

    j = P+i #[0:8] , [1:9] P =8
    print(f"i : {i}")
    print(f"j : {j}")
    if j <= P+1:
        DNA_cut = DNA[i:j]
        print("DNA CUT : " ,DNA_cut)
        d = dict(Counter(DNA_cut))
        p=0
        res+=1
        for k,v in d.items():
            
            print(f'find3[{k}] : {find3[k]}')
            print(f'd[{k}] : {d[k]}')
            if d[k] < find3[k]:
                res-=1
                break


                
print(res)
#%%
