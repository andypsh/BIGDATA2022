# import sys
#
# croatia = ['c=' , 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=']
# a = str(sys.stdin.readline().rstrip())
# print(len(a))
# sum =0
# for i in range(len(croatia)):
#     sum += a.count(croatia[i])
# d = len(a) - sum
# print(d)
# alphabet = []
# for i in range(97,123):
#     alphabet.append(chr(i))
# res =0
# B = list(A)

# print(res)
import sys


alpha = str(sys.stdin.readline().rstrip())
print("alpha : " , alpha)
croatia = ['c=', 'c-', 'dz=' , 'd-', 'lj' , 'nj' , 's=' ,'z=']
sum =0
for i in range(len(croatia)):
    print(croatia[i] , ': ' , alpha.count(croatia[i]))
    sum+=alpha.count(croatia[i])
    #string 형태로 저장되어있는 c안에 croatia리스트 안의 요소값의 개수를 세어보라

print(len(alpha) - sum) #기존 alpha의 값에서 dz= ==> 한단어로 취급
