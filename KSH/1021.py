from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))
dN = deque([i for i in range(1, N + 1)])
count = 0
for i in A:
    while True:
        if(dN[0] == i):
            dN.popleft()
            break
        else:
            if(dN.index(i) <= len(dN) / 2):
                dN.rotate(-1)
                count += 1
            else:
                dN.rotate(1)
                count += 1
print(count)