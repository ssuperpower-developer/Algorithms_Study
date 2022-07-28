from collections import deque

t = int(input())

def bfs(start, cnt_plane):
    dq= deque()
    dq.append(start)
    visited[start] = True

    while dq:
        if visited.count(True) == n :
            return cnt_plane

        current_node = dq.popleft()

        for node in graph[current_node]:
            if visited[node]==False :
                dq.append(node)
                visited[node] = True
                cnt_plane +=1



for i in range(t):
    #국가의 수n 비행기의 종류 m
    n, m = map(int,input().split())
    visited = [False]*(n+1)

    graph = [[] for i in range(n+1)]

    for j in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    print(bfs(1,0))



