import sys

M = list(map(int , sys.stdin.readline().split(' ')))

N = M[1]







prefix_2 = [ [0 for i in range(5)]]
for k in range(M[0]):
    a = 0
    prefix = [0]
    Nums = list(map(int , sys.stdin.readline().split(' ')))
    for i in range(M[0]):
        a += Nums[i]
        prefix.append(a)
    prefix_2.append(prefix)
# print(prefix_2)
# print(prefix_2[1][-1])
res = []
for i in range(N): #결과값 횟수
    RES = list(map(int , sys.stdin.readline().split(' ')))
    x_1 = RES[0]
    y_1 = RES[1]
    x_2 = RES[2]
    y_2 = RES[3]
    b = 0
    for k in range(x_1 , x_2+1):
        # print("prefix_2[{}][y_1] :{}".format(k, prefix_2[k][y_1]))
        # print("prefix_2[{}][y_2 - y_1] :{}".format(k , prefix_2[k][y_2 - y_1]))
        b += prefix_2[k][y_2] - prefix_2[k][y_1 - 1]

    print(b)


#%%
