T= int(input())
for i in range(T):
    R, S = map(str, input().split())
    for j in S:
        for k in range(int(R)):
            print(j, end = "")
    print()