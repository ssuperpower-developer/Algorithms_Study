import sys
T = int(sys.stdin.readline())
for i in range(T):
    floor = int(sys.stdin.readline())
    num = int(sys.stdin.readline())
    new_floor = [i for i in range(1, num + 1)]
    for j in range(floor):
        next_floor = []
        for k in range(num):
            next_floor.append(sum(new_floor[:k + 1]))
        new_floor = next_floor.copy()
    print(new_floor[-1])
