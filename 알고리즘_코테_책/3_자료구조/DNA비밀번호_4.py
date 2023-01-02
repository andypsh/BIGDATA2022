import sys

S, P = map(int, sys.stdin.readline().split())
dna = list(sys.stdin.readline().rstrip())
# tmp = list(map(int, sys.stdin.readline().split()))
dic = dict(zip(['A' , 'C' ,'G' , 'T'] ,list(map(int, sys.stdin.readline().split(' ')))))
base = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

count = 0
for i in range(S-P+1): #S=4 , P=2 ==> range(3) ==> [0,1,2]
    flag = True

    if i == 0:
        for j in range(P): #P=2 ==> range(2) ==> [0,1]
            base[dna[j]] += 1 #base[dna[0]] ==> base['G']  , base[dna[1]] ==> base['A']
    else:
        base[dna[i+P-1]] += 1 # base[dna[1+2-1]] = base[dna[2]] = base['T'] +=1
        base[dna[i-1]] -= 1 # base[dna[1-1]] -=1 = base[dna[0]] = base['G'] -= 1

    for i in ('A', 'C', 'G', 'T'):
        if base[i] < dic[i]:
            flag = False
            break

    if flag:
        count += 1

print(count)
#%%
