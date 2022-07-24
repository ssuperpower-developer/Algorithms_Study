import sys

N = int(sys.stdin.readline())
arry = [0]*10000

for i in range(N):
    n = int(sys.stdin.readline())
    arry[n-1] += 1

for i in range(len(arry)):
    if arry[i]!=0:
        for j in range(arry[i]):
            print(i+1)


