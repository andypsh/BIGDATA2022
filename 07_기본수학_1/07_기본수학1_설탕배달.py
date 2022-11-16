import sys

#설탕 봉지는 3kg , 5kg 봉지

#5x+3y = N

# 22g 5kg 봉지==> 22-(5*4(개)) ==2 22-(5*3(개)) == 7 22-(5*2(개)) == 12
# 6KG 5kg 봉지 ==? 6-(5*1(개)) ==1
N = int(sys.stdin.readline())
a = N//5 #첫 갯수
#print('a : ' ,a)
res = 0

if N%5 ==0:
    res += (N//5)
else:
    while True:
        B = N -(5*a)
        #print('B : ', B)
    
        if B%3 ==0:
            res+= a+ (B//3)
            break
        elif B%3 !=0:
            a-=1
        if a <= 0 :
            if N%3 == 0:
                res += N//3
            else:
                res = -1
            break
print(res)





# while True:
#     if a!= 0:
#         B = B - (5*a)
#         print("B : ",B)
#         if B != 0:
#             if B%3 ==0:
#                 res = a+(B//3)
#
#             else:
#                 a-=1
#         else:
#             res = a
#     elif a == 0 :
#         if B%3 == 0:
#             res = (B//3)
#         else:
#             print('-1')
#         break
    # N = N-(5*a)
    # print("N : " , N)
    # if a==0:
    #     if N%3 == 0:
    #         res = N//3
    #     else:
    #         print("-1")
    #     break
    # if N%3 == 0:
    #     res = a+(N//3)
    #     print(res)
    #     break
    # elif N%3 !=0:
    #     a-=1





