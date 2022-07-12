testingNum=int(input())
for i in range(testingNum):
    repeatNum,string=map(str,input().split())
    for j in string:
        for k in range(int(repeatNum)):
            print(j,end='')
    print()

















