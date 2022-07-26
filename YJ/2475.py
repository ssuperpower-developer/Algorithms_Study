def to_SquareNumber(x):
    return x**2

#map(적용시킬 함수, 적용할 값들)
A = list(map(int, input().split()))
N = list(map(to_SquareNumber,A))
# N=list(map(lambda:x**2,A))

X=0
for i in N:
    X+=i
print(X%10)