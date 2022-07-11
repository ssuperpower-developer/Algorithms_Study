n,x=map(int,input().split())
nlist=list(map(int,input().split()))
nlist=[num for num in nlist if num<x]
for i in nlist:
    print(i,end=' ')
'''print(' '.join(map(str,nlist)))'''