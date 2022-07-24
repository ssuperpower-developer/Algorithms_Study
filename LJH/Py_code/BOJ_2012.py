import sys
input = sys.stdin.readline
N = int(input())
arry = [int(input()) for i in range(N)]
arry_sort = sorted(arry)
temp = 0
for i in range(len(arry)):
    temp += abs((i+1) - arry_sort[i])

print(temp)
