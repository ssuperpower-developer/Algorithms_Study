from collections import deque


N = int(input())
q = [i for i in range(1, N + 1)]
dq = deque(q)
for i in range(N - 1):
    dq.popleft()
    dq.rotate(-1)
print(dq[0])
