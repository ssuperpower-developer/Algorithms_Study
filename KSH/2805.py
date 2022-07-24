import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, input().split()))
start = 1
end = sum(trees)
while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in trees:
        if i >= mid:
            result += i - mid
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
sys.stdout.write(str(end))