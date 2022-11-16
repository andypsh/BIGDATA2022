import sys

N = int(sys.stdin.readline())

#2 4 -10 4 -9
#2는 -10 -9로 2개
#4는 2 -10 09로 3개
#-10은 0개
#4는 3개
#-9는 1개
A = list(map(int, sys.stdin.readline().rstrip().split()))

B = sorted(list(set(A)) , reverse= False)
dic = {}
for i in range(len(B)):
    dic[B[i]] = i
    #B[0] = -10 : 0
    #B[1] = -9 : 1
    #B[2] = 2 : 2
    #B[3] = 4 : 3
for i in A:
    print(dic[i] , end = ' ')
    #dic[2] = 2
    #dic[4] = 3


#%%
