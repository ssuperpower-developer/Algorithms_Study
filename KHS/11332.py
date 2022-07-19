from math import factorial, log10,log2

def O_n(N,T,L):
    if (log10(N*T)<=8+log10(L)):
        return "May Pass."
    else:
        return "TLE!"

def O_n3(N,T,L):
    if (3*log10(N)+log10(T)<=8+log10(L)):
        return "May Pass."
    else: return "TLE!"

def O_n2(N,T,L):
    if (2*log10(N)+log10(T)<=8+log10(L)):
        return "May Pass."
    else:
        return "TLE!"

def O_nFact(N,T,L):
    if(T*log10(factorial(N))<=8+log10(L)):
        return"May Pass."
    else:
        return "TLE!"
    
def O_2(N,T,L):
    if (N+log2(T)<=8*(1+log2(5)+log2(L))):
        return"May Pass."
    else:
        return "TLE!"
a=[]
for i in range(int(input())):
    S,N,T,L=map(str,input().split())
    if S=="O(N)":
        a.append(O_n(int(N),int(T),int(L)))
    elif S=="O(N^2)":
        a.append(O_n2(int(N),int(T),int(L)))
    elif S=="O(N^3)":
        a.append(O_n3(int(N),int(T),int(L)))
    elif S=="O(2^N)":
        a.append(O_2(int(N),int(T),int(L)))
    elif S=="O(N!)":
        a.append(O_nFact(int(N),int(T),int(L)))

for i in a:
    print(i)