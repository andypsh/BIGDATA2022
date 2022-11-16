# # def self_number(n):
# #     a = n
# #     sum = a
# def self_number(a):
#     sum = 0
#     b =a
#
#     while True:
#         if a>=1000:
#             sum+=a//1000
#             a = a-((a//1000)*1000)
#
#         elif a>= 100 and a<1000:
#             sum+=a//100
#             a = a-((a//100)*100)
#
#         elif a>= 10 and  a<100:
#             sum+=a//10
#             a = a-((a//10)*10)
#
#         elif a>= 1 and a<10:
#             sum+=a
#             break
#     sum += b
#     print(sum)
#     if sum <10000:
#         self_number(sum)
# #print(a//2)
#
# self_number(1)

# def self_number(n):
#     A= []
#     for i in range(1,10001):
#         A.append(i)
#     b = list(map(int, list(str(n))))
#     c = sum(b[:]) + n
#
#
#
#
# self_number(1)

def solution(n):
    all , self_num , self_num_2= [] , [] , []
    for i in range(n):
        sum = 0
        sum+= i
        self_num.append(i) #1부터 10000까지의 숫자 리스트화
        b = list(str(i)) #b 리스트에 ['1', '2' ,'3'] 식으로 저장
        for j in b:
            sum+=int(j) #sum 변수에 값들 더하기
        if sum < n: #sum값이 123보다 작으면
            all.append(sum) #all 리스트에 sum값 넣기
    for k in range(len(self_num)):
        if self_num[k]  in all:
            continue
        else:
            self_num_2.append(self_num[k])
    return self_num_2
for i in solution(10000):
    print(i)