import sys
N = int(input())
rope = [int(sys.stdin.readline().rstrip()) for i in range(N)]
rope.sort()
result = []
for i in range(N):
    result.append(int(rope[i]) * (N - i))
print(max(result))
