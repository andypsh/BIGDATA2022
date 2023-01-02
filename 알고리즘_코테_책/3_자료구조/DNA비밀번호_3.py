import sys

checkList = [0] * 4
myList=  [0] * 4
checkSecret  = 0

#함수 정의
def myadd(c): #새로 들어온 문자를 처리하는 함수
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] +=1
        if myList[0] == checkList[0]:
            checkSecret+= 1

    elif c == 'C':
        myList[1] +=1
        if myList[1] == checkList[1]:
            checkSecret+= 1

    elif c == 'G':
        myList[2] +=1
        if myList[2] == checkList[2]:
            checkSecret+= 1

    elif c == 'T':
        myList[3] +=1
        if myList[3] == checkList[3]:
            checkSecret+= 1

def myremove(c):
    global checkList , myList, checkSecret
    if c == 'A':
        myList[0] -=1
        if myList[0] == checkList[0]:
            checkSecret-= 1

    elif c == 'C':
        myList[1] -=1
        if myList[1] == checkList[1]:
            checkSecret-= 1

    elif c == 'G':
        myList[2] -=1
        if myList[2] == checkList[2]:
            checkSecret-= 1

    elif c == 'T':
        myList[3] -=1
        if myList[3] == checkList[3]:
            checkSecret-= 1

S, P = map(int , sys.stdin.readline().split(' '))
A = list(sys.stdin.readline().rstrip())
checkList =list(map(int, sys.stdin.readline().split(' ')))
Result = 0
#find = dict(zip(['A' , 'C' ,'G' , 'T'] ,list(map(int, sys.stdin.readline().split(' ')))))

for i in range(4):
    if checkList[i] == 0:
        checkSecret +=1
for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result +=1

for i in range(P,5):
    j = i - P
    #P=2  , 5
    #j = 2- 2 = 0
    #myadd(A[2])
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result +=1
print(Result)
#%%
