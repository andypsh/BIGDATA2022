import sys

A = list(str(sys.stdin.readline().rstrip()))

# print(ord('A'))
# print(ord('Z'))
alphabet_1= []
alphabet_2= []
dial , dial_2= [] , []
for i in range(65,80):
    alphabet_1.append(chr(i))
for i in range(80,91):
    alphabet_2.append(chr(i))
for i in range(5):
    dial.append(alphabet_1[i*3:(i+1)*3])
for i in range(1):
    dial.append(alphabet_2[i*4:(i+1)*4])

dial.append(alphabet_2[4:7])
dial.append(alphabet_2[7:11])
print("dial:" , dial)
res = 0


for j in range(len(A)):
    for i in range(len(dial)):
        if A[j] in dial[i] :
            res+= (3+i)
            break


print("res:" , res)

