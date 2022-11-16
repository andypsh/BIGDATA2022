import sys

N = int(sys.stdin.readline()) #72
M=N # M = 72
i=2
A=[]
while i<=N: #1 ) 2<= 72 2) 2<= 36
    if M%i==0: #72%2 == 0 36%2 == 0
        M = M//i #M = 72//2 = 36 M = 36//2 = 18
        A.append(i)
    else:
        i+=1

A= sorted(A)
for i in A:
    print(i)


#%%
