import sys

def recursion(s, l, r):
    if l >= r: return [1 , l+1] #
    elif s[l] != s[r]: return [0 , l+1] #일치하지 않으면 호출 x
    else: return recursion(s, l+1, r-1) #재귀로 호출 더

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(sys.stdin.readline())
#print(isPalindrome('aaa'))
res = []
for i in range(N):
    A = str(sys.stdin.readline().rstrip())
    res.append(isPalindrome(A))
for p in range(len(res)):
    for k in res[p]:
        print(k , end = ' ')
    print('')
#isPalindrome('ABBA')
#recursion('ABBA', 0 , 4-1 = 3) l=0 <r=3 s[0] =A == s[3] ==A
# else return recursion('ABBA', l+1 = 1 , r-1 = 2)
#recursion('ABBA' , 1, 2) 1< 2 s[1] = B == s[2] ==B
#return recursion('ABBA' , 2, 1) ==> return print(1 , l=2)
#%%
