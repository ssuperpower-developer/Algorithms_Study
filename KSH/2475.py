N = list(map(int, input().split()))
A = [i**2 for i in N]
print(sum(A) % 10)