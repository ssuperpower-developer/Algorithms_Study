import readline
import sys
N = int(input())
A = list(0 for i in range(10001))
for i in range(N):
    a = int(sys.stdin.readline())
    A[a] += 1
for i in range(1, 10001):
    for j in range(A[i]):
        print(i)