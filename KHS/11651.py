import sys
N=int(sys.stdin.readline())
a=[]
for i in range(N):
    a.append(tuple(map(int,sys.stdin.readline().split())))
for k,p in sorted(a,key=lambda a:(a[1],a[0])):
    print(k,p)