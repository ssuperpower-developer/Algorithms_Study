#sort를 쓰면 메모리가 초과됨
#다른 문제 풀 때도 썼던 방법을 응용 (인덱스 번호를 기준으로 숫자를 1 증가하는것과 비슷하게)
#해당 숫자의 개수를 배열에 넣고, 숫자의 개수만큼 출력!
import sys
N = int(sys.stdin.readline())
A = [0] * 10001 #이 수는 10,000보다 작거나 같은 자연수이다.
for i in range(N):
    A[int(sys.stdin.readline())] += 1
for i in range(10001):
    if A[i] != 0:
        for j in range(A[i]):
            print(i)
