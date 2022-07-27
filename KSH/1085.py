A = list(map(int, input().split()))
B = [A[0], A[1], A[2] - A[0], A[3] - A[1]]
print(min(B))