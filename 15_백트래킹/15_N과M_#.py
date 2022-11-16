import sys
def ret():

    if len(s) == 5:
        res.append(s)
        # a = ' '.join(map(str, s))
        return res
    i = 0
    s.append(i+1)
    ret()

s = []
res = []
print(ret())
# res.append(ret())
# print(res)

#%%
