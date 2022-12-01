import sys

N=sys.stdin.readline()
A = sorted(map(int,sys.stdin.readline().split()))
#이진탐색은 정렬되어 있는 경우에만 가능!
M=sys.stdin.readline()
B = map(int,sys.stdin.readline().split())


def binary(l,A,start,end):
    if start>end:
        return 0
    M=(start+end)//2

    if l==A[M]:
        return 1
    elif l<A[M]:
        return binary(1,A,start,M-1)
    else:
        return binary(1,A,M+1,end)

for l in B:
    start=0
    end=len(A)-1
    print(binary(l,A,start,end))