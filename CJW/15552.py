#반복문으로 여러줄 입력받는 상황에서는 sys.stdin.readline()으로 시간초과 방지
import sys

for i in range(int(input())):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)