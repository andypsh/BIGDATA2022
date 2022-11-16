import sys

T = list(map(int, sys.stdin.readline().rstrip().split()))

A = T[0]
B = T[1]
C = T[2]
if B>=C:
    print("-1")
else:
    notebook_gaet = A//(C-B)
    #print("notebook_gaet : " , notebook_gaet)
    if notebook_gaet * (C-B) <= A :
        notebook_gaet+=1



    print(notebook_gaet)