from collections import deque
import sys
N = sys.stdin.readline()
q = deque(enumerate(list(map(int, input().split()))))
result = []
while(q):
    index, paper = q.popleft()
    result.append(index + 1)
    if(paper > 0):
        q.rotate(-paper + 1)
    else:
        q.rotate(-paper)
print(' '.join(map(str, result)))