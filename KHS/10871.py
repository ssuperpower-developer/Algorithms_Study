N,X=map(int,input().split())
A=list(map(int,input().split()))
A=[i for i in A if i<X]
for t in A:
    print(t,end=' ')