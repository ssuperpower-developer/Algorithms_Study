from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque(map(int, input().split()))
ballon_list = []

dq_game = dq.copy()
while dq_game:
    target = dq_game[0]
    print(target)
    dq_game.rotate(-target)
    ballon_list.append((dq_game.index(target))+1)
    dq_game.remove(target)    
    print(dq_game)

print(*ballon_list)

