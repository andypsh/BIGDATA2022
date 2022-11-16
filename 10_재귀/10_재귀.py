import sys

def fact(n):

    if n > 1:
        return n*fact(n-1)
    else :
        return 1
a = int(sys.stdin.readline())
print(fact(a))

# fact (10) = 10*fact(9)
# fact(9) = 9*fact(8)
#
#
#
# fact(2) = 2*fact(1)
# fact(1) = 1

#%%
