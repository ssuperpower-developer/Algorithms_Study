a = list(map(int,(input().split())))
sumNum = [i*i for i in a]
print(sum(sumNum)%10)
