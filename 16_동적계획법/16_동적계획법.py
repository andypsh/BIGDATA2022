import sys

def fib(n) :
    if n == 1 or n == 2 :
        return 1  # 코드1
    else :
        return (fib(n - 1) + fib(n - 2))



def fibonacci(n):
    f=[1,1]
    a=n
    if n>2:
        for i in range(2,n):
            f.append(f[i-1] + f[i-2])
    #print(f)
    return len(f)-2
n = int(sys.stdin.readline())
b = fibonacci(n)
c= fib(n)
print('{} {}'.format(c,b),end=' ')

#%%
