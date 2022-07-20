import sys

N=int(input())

grade = [int(sys.stdin.readline()) for x in range(N)]

grade.sort()

result=0 #불만족도의 합
for i in range(1,N+1):
    result+=abs(i-grade[i-1])
print(result)