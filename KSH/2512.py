import sys
N = sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
start = 0
end = max(A)
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in A:
        if i > mid:
            result += mid
        else:
            result += i
    if result > M:
        end = mid - 1
    else:
        start = mid + 1
sys.stdout.write(str(end))
