from collections import deque
import sys
N = int(input())
dq = deque()
result = []
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        dq.appendleft(command[1])
    elif command[0] == "push_back":
        dq.append(command[1])
    elif command[0] == "pop_front":
        if dq:
            result.append(dq[0])
            dq.popleft()
        else:
            result.append("-1")
    elif command[0] == "pop_back":
        if dq:
            result.append(dq[len(dq) - 1])
            dq.pop()
        else:
            result.append("-1")
    elif command[0] == "size":
        result.append(len(dq))
    elif command[0] == "empty":
        if dq:
            result.append("0")
        else:
            result.append("1")
    elif command[0] == "front":
        if len(dq) == 0:
            result.append("-1")
        else:
            result.append(dq[0])
    elif command[0] == "back":
        if len(dq) == 0:
            result.append("-1")
        else:
            result.append(dq[len(dq) - 1])
print("\n".join(map(str, result)))