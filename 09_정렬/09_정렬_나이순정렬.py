import sys

N = int(sys.stdin.readline())
res =[]
for i in range(N):

    a = list((sys.stdin.readline().rstrip().split(' ')))
    a[0] = int(a[0])
    # for j in a[1]:
    #     b.append(str(j))
    #print(b)
    #a.pop()
    #a.append(b)
    res.append(a)
res.sort(key = lambda x : (x[0]))

#print(res)

for i in res:
    #str = ''
    for p in i:
        #if p ==1 :
            #for k in i[p]:
                #str+=k
        print(p , end = ' ')
    print('')
#%%
