import sys
N=int(sys.stdin.readline())
a=[]

for i in range(N):
    a.append(int(sys.stdin.readline().rstrip()))

checker=0

for k,v in enumerate(sorted(a)):# 앞이 인덱스
    if v!=k+1:
        checker+=abs(v-k-1)

print(checker)