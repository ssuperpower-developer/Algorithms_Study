from math import factorial

def time_Complexity(S,N,T,L):
    L*=10**8
    if(S == "O(N)"):
        if(N*T <= L):
            return "May Pass."
        else:
            return "TLE!"
    elif(S == "O(N^2)"):
        if(N**2*T <= L):
            return "May Pass."
        else:
            return "TLE!"
    elif (S == "O(N^3)"):
        if(N**3*T <= L):
            return "May Pass."
        else:
            return "TLE!"
    elif(S == "O(2^N)"):
        if(2**N*T <= L):
            return "May Pass."
        else:
            return "TLE!"
    elif (S == "O(N!)"):
        if(factorial(N)*T <= L):
            return "May Pass."
        else:
            return "TLE!"
    else:
        return "Wrong input"

case = int(input())
for i in range(case):
    S,N,T,L = input().split()
    print(time_Complexity(S,int(N),int(T),int(L)))

'''
시간초과 발생
def factorial(N):
    result = 1
    for i in range(1, N+1):
        result*=i
    return result
'''