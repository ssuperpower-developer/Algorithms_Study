L = int(input())
string = input()
sum=0

for i in range(L):
    sum += (ord(string[i])-96) * (31 ** i) #ord함수 : 아스키코드 값
    #a 기준으로 아스키코드는 97이므로 96을 뺌
print(sum % 1234567891) #나누는 수를 1234567891라고 문제에서 나옴