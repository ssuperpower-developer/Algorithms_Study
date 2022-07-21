a,b=map(int,input().split())


#최대공약수
for i in range(min(a,b),0,-1): 
    #a와 b 중 작은 숫자부터 1까지, 1씩 감소하며, a와 b를 i로 나눔
    #두 수를 모두 나눌 수 있는 약수 중 가장 큰 수
    if a%i==0 and b%i==0:
        print(i)
        break

#최소공배수
for i in range(max(a,b),(a*b)+1):
    #a와 b 중 큰 숫자부터 둘의 곱까지, 1씩 증가하며, i를 a와 b를 나눔
    if i%a==0 and i%b==0:
        print(i)
        break