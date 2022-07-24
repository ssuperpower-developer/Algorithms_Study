import sys

expectedlist=[]
N = int(input())
for i in range(N):
    expectedlist.append(int(sys.stdin.readline()))
expectedlist.sort()

value=0
for i in range(N):
    value += abs(expectedlist[i]-(i+1))
print(value)