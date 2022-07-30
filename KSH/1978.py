import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
count = 0
for i in A:
    none_prime = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            none_prime += 1
    if none_prime == 0:
        count += 1
print(count)
