import sys

def w(a,b,c):

    if a <= 0 or b <= 0 or c <= 0 :
        return 1

    elif a > 20 or b > 20 or c > 20 :
        return w(20, 20, 20)

    elif a < b and b < c :
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else :
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
res= []
while True:
    a = list(map(int,sys.stdin.readline().split()))
    if (a[0] == -1 and a[1] == -1) and a[2]== -1 :
        break
    else:
        print("w({},{},{}) = {}".format(a[0],a[1],a[2],w(a[0],a[1],a[2])))
# for i in res:
#     print(i)

# a,b = map(int ,sys.stdin.readline().split())
# print(a)
# print(b)
# print(b)

#%%
