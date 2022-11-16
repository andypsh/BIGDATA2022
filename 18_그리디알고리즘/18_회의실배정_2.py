import sys

A = int(sys.stdin.readline())
B=[]
for i in range(A):
    c = list(map(int,sys.stdin.readline().split()))
    B.append(c)

B = sorted(B, key = lambda x : x[0] )
C = sorted(B , key = lambda x : x[1])
# print(B)
# print(C)

last = 0
count = 0
for i in C:
    if i[0] >= last: #i[0] = 1 last = 0 ==> last = 4 count =1
        #i[0] = 3 last =4 X
        #i[0] = 0 last = 4 X
        #i[0] = 5 last = 4 ==> last = 5 count =2



        print([i[0] , i[1]])
        last = i[1]
        count+=1
print(count)

#%%
