#python

#rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 
# 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다. 
# 즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다.
#  참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

#Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.

# import sys
# T=int(input())
# for i in range(T):
#     A,B=map(int, sys.stdin.readline)
#     print(A+B)

import sys
T = int(sys.stdin.readline())
for i in range(T):
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    print(A[0] + A[1])