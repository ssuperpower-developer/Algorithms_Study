#카운팅 리스트 사용 문제
import sys

N = int(sys.stdin.readline())
arr = [0]*10001

for i in range(N):
    arr[int(sys.stdin.readline())]+=1

for i in range(1,10001):
    if arr[i]!=0:
        for _ in range(arr[i]):
            print(i)


'''
#Unpacking Operator *
import sys

N = int(input())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr.sort()
print(*arr,sep='\n')
'''



