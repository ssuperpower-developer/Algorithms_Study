A=list(map(int,input().split()))
A=[i**2 for i in A]
print(sum(A)%10)