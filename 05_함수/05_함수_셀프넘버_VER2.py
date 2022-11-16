import sys


def d(n):

    A = list(map(int , str(n)))

    b = n+sum(A)
    if n!=b:
        print(b)
        return d(b)
    else:
        print("end : {}".format(n))
d(354)


#%%
