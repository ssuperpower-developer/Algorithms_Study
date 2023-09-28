#풍선 터트리기 펑펑
from collections import deque
import sys
N=int(input())
a=deque(map(int,sys.stdin.readline().split()))

# for i in range(5):
#     a.append(int(input()))
# for i in a:
#     print(i,end=" ")
indexcheck=0
temp=0
while a:
    print(temp)
    indexcheck+=a[temp]
    a.remove(a[temp])
    if temp>len(a)-1:
        temp-=len(a)
    elif temp<-len(a):
        temp+=len(a)
