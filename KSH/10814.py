import sys
N = int(sys.stdin.readline().rstrip())
information = []
for i in range(N):
    information.append(sys.stdin.readline().split())
information.sort(key=lambda x: int(x[0]))
for i in range(N):
    print(information[i][0], information[i][1])
