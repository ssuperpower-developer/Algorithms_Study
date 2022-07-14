# n = int(input())
# [print((" ")*(n-(i+1)) + ("*")*(i+1)) for i in range(n)]

n = int(input())
[print((" ")*(n-i) + ("*")*i) for i in range(1,n+1)]