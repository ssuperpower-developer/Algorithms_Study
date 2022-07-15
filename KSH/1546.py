N = int(input())
A = list(map(int, input().split()))
A = [i / max(A) * 100 for i in A]
print(sum(A) / N)