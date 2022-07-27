N, X = map(int, input().split())
c = list(map(int, input().split()))
for i in range(N): 
    if (c[i] < X): print(c[i], end = " ")
