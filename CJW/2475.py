data = list(map(int,input().split()))
power = [num*num for num in data]

print(sum(power)%10)