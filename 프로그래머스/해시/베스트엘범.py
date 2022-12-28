
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}
    print("list(zip(genres, plays)) : {}".format(list(zip(genres, plays))))
    for i, (g, p) in enumerate(zip(genres, plays)):
        #i = 0 g= 'classic' p = 500
        #i= 1 g= 'pop' p =600
        #i=2 g= 'classic' p =150
        #i=3 g= 'classic' p =800
        #i= 4 g= 'pop' p =2500
        if g not in dic1: #'classic' in dic1 , 'pop' in dic1
            dic1[g] = [(i, p)]

            #dic1['classic'] = [(0,500)]
            #dic1['pop'] = [(1,600)]
        else:
            dic1[g].append((i, p))

            #dic1['classic'].append((2,150)) ==> dic1 {'classic' : [(0,500), (1,600)] ,'pop' : [(1,600)]}
            #dic1['classic'].append((3,800)) ==> dic1 {'classic' : [(0,500), (1,600), (3,800)] ,'pop' : [(1,600)]}
            #dic1['pop'].append((4,2500)) ==> dic1 {'classic' : [(0,500), (1,600), (3,800)] ,'pop' : [(1,600) , (4,2500)]}
        print("dic1 : {}".format(dic1))
        if g not in dic2: #classic in dic2
            dic2[g] = p

            #dic2['classic'] = 500
            #dic2['pop'] = 600
        else:
            dic2[g] += p
            #dic2['classic'] += 600 ==> {'classic' : 500+600 , 'pop' : 600}
            #dic2['classic'] += 800 ==> {'classic' : 500+600+800 , 'pop' : 600}
            #dic2['pop'] += 600 ==> {'classic' : 500+600+800 , 'pop' : 600+2500}
        print("dic2 : {}".format(dic2))
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        #sorted(dic2.items()) ==> {'classic' : 2100 , 'pop' : 3100}
        #key = lambda x:x[1] ==> 숫자들로 정렬 하겠다.
        #k = 'pop' , 'classic'
        #v = 3100 , 2100
        print("dic1 : {}".format(dic1[k]))
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            #장르 별로 가장 많이 재생된 노래를 최대 2개까지 모아 베스트엘범 출시 하므로
            print("dic1_i : {}".format(i))
            print("dic1_p : {}".format(p))
            #sorted(dic1['pop']) = [(1,600) , (4,2500)]
            #sorted(dic1['pop'], key=lambda x:x[1], reverse=True)[:2] = [(4,2500) , (1,600)]

            answer.append(i)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"] , [500, 600, 150, 800, 2500]))
#%%
