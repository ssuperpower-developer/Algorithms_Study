import sys
# sys.setrecursionlimit(10**7)


def dfs(node, cnt):
    check[node] = 1
    for i in graph[node]:
        if check[i] == 0:
            cnt = dfs(i, cnt + 1)
    return cnt


T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    for j in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    check = [0] * (N + 1)
    check[1] = 0
    result = dfs(1, 0)
    print(result)
