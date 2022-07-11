N, X = map(int, input().split())
A = list(map(int, input().split()))
A = [i for i in A if i < X]
for i in A:
    print(i, end = ' ')