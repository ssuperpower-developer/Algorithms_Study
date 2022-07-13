# 10871
#map(적용시킬 함수, 적용할 값들)
N, X = map(int, input().split())
A = list(map(int, input().split()))
A = [i for i in A if i < X]
# [i for i in A if i<X] 
# 리스트 표현식
# [식 for 변수 in 리스트]
# list(식 for 변수 in 리스트)
for i in A:
    print(i, end = ' ')