import sys

A = list(map(str, sys.stdin.readline().rstrip()))
#print(ord('a'))
#print(ord('z'))
alphabet = []
for i in range(97,123):
    alphabet.append(chr(i))

print(alphabet)
res = []

for i in alphabet:
    if i in set(A):
        idx = A.index(i)
        res.append(idx)
    else:
        res.append(-1)
res2= ''
for i in res:
    res2 += (str(i)+ " ")
print(res2)
# for i in alphabet:
#     if i
