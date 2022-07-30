import sys
N = int(input())
A = list(set([sys.stdin.readline().rstrip() for i in range(N)]))
A.sort()
A.sort(key = lambda x : len(x))
print('\n'.join(A))