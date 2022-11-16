import sys

A = int(sys.stdin.readline())
stack = []
B = []
#스택은 LIFO 형태로 먼저들어온게 뒤에 들어가있는다. 나중에 들어온게 처음에 들어가있고.
for i in range(A):
    c = list(map(str, sys.stdin.readline().rstrip().split()))

    if c[0] == 'push':
        c[1] = int(c[1])
        stack.append(c[1])
    elif c[0] =='pop' :
        if len(stack)>=1:
            print(stack.pop())
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        if len(stack)>=1:
            print(0)
        else:
            print(1)
    elif c[0] == 'top':
        if len(stack)>=1:
            print(stack[-1])
        else:
            print(-1)




#%%
