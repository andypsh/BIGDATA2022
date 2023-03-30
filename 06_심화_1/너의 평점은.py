import sys

score = ['A+' , 'A0' ,'B+' , 'B0' , 'C+','C0','D+','D0','F']
pyeong = [4.5 , 4.0 , 3.5 , 3.0 , 2.5 , 2.0 , 1.5 , 1.0 , 0.0]
isu_hak = 0
hak = 0
for i in range(20):
    A= list(sys.stdin.readline().split())
    if A[2]!='P':
        hak+= pyeong[score.index(A[2])] * float(A[1])
        isu_hak += float(A[1])
print(hak/ (isu_hak))