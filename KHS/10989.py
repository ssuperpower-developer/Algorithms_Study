# a=[]
# for i in range(int(input())):
#     a.append(int(input()))
# a=[int(input()) for i in range(int(input()))]
# for i in sorted(a):
#     print(i)
import sys
N=int(sys.stdin.readline())
ary=[0]*10001

for i in range(N):
    temp=int(sys.stdin.readline())
    ary[temp]+=1

for k in range(10001):
    if ary[k]!=0:
        for t in range(ary[k]):
            print(k)