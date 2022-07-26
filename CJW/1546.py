n=int(input())
data=list(map(int,input().split()))
M=max(data)
data=[score/M*100 for score in data]
print(sum(data)/n)