import sys

n=int(sys.stdin.readline())
my_list = [sys.stdin.readline().strip() for i in range(n)]

my_list.sort()
my_list.sort(key=lambda i:len(i))
print(my_list)