#그 다음 C개의 줄에는 시간 복잡도를 나타내는 문자열 S, 
# 각 테스트 케이스마다 입력의 최대 범위 N, 
# 테스트 케이스의 수를 나타내는 T랑 제한시간(초 단위) 를 나타내는 L이 주어진다. 
# (1 <= C <= 100, 1 <= N <= 1000000, 1 <= T, L <= 10, N, T, L은 정수)

import sys

def Factorial(N,T,L):
    start=T
    for i in range(1,N+1):
        start*=i
        if start>(10**8)*L : return False
    return True
def Solution(S,N,T,L):
    N=int(N)
    T=int(T)
    L=int(L)

    if S=='O(N)':
        BigO=N*T
    elif S=='O(2^N)':
        BigO=(2**N)*T
    elif S == 'O(N^3)':
        BigO=(N**3)*T
    elif S == 'O(N^2)':
        BigO = (N**2) * T
    elif S == 'O(N!)':
        return Factorial(N,T,L)
        # BigO=Factorial(N)*T
        # math.factorial(N)*T
    if (10**8)*L<BigO:return False
    else: return True

C=int(input())

for _ in range(C):
    S,N,T,L=sys.stdin.readline().split()
    if Solution(S,N,T,L) :
        print("May Pass.")
    else :
        print("TLE!")