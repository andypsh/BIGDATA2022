import sys

A = int(sys.stdin.readline())
res , res2 = [] ,[]
stack = []
first_len = 0
for i in range(A):
    res = ""
    idx =""
    res = str(sys.stdin.readline().rstrip()) #입력 : (()) ==> res = "((())"
    idx = res
    #B = res.split('()')
    while True:
        if '()' in idx: #idx= '((())'
            B = idx.split('()') # ()를 기준으로 나눈 list 화 ['(' ,'']
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
    #
    # print(res)
    # # for i in list(set(res)):
    # #     d+=i
    # #print(res)
    # #print(d)
    # while True:
    #     if idx == res:
    #         break
    #     else:
    #         idx = res
    #         res =''
    #         for i in B:
    #             if i != '':
    #                 res +=i
    #                 #print(res)
    #     B = list(res.split('()'))
        #print(B)
    # if '' not in B:
    #     res2.append('NO')
    # else:
    #     res2.append('YES')

    # c = str(sys.stdin.readline().rstrip().split('()'))
    # B = list(map(str, c))
#print(B)

#print(C)


#%%
