import sys
a = [int(sys.stdin.readline().rstrip()) for i in range(int(sys.stdin.readline().rstrip()))]
a.sort()
b = [abs(int(a[i]) - i - 1) for i in range(len(a))]
print(sum(b))