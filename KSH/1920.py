import sys
n = sys.stdin.readline().rstrip()
N = set(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline().rstrip()
M = list(map(int, sys.stdin.readline().split()))
for i in M:
    if i in N:
        print('1')
    else:
        print('0')