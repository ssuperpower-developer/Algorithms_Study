import sys
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    while(True):
        if(A > B):
            A //= 2
        elif(A < B):
            B //= 2
        else:
            print(A * 10)
            break
