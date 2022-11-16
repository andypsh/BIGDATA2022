import sys

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#n=20
#n=10
##0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
def Fibo(n):

    if 0<n<=2:
        return 1
    elif n==0:
        return 0
    else:
        return Fibo(n-1) + Fibo(n-2)
a=int(sys.stdin.readline())
print(Fibo(a))
#Fibo(10) = Fibo(9) + Fibo(8)

#Fibo(9) = Fibo(8) + Fibo(7)


#Fibo(3) = Fibo(2) + Fibo(1) = 1+ 1 =2
#Fibo(2) = Fibo(1) + Fibo(0) = 1
#Fibo(1) = 1
#Fibo(0) = 0

#%%
