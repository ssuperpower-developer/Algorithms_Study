import sys

def binary(input):
    if input==1:
        return input
    elif input%2==1:
        return int((input-1)/2)
    elif input%2==0:
        return int(input/2)

a=[list(map(int,sys.stdin.readline().split())) for i in range(int(input()))]
b=[]
c=[]
d=[]
for i,k in a:
    b.append(i)
    c.append(k)
    while True :
        if i==1 and k==1:
            break
        elif i==1:
            k=binary(k)
            c.append(k)
        elif k==1:
            i=binary(i)
            b.append(i)
        else:
            k=binary(k)
            c.append(k)
            i=binary(i)
            b.append(i)
    print(10*max(set(b)& set(c)))
    b.clear()
    c.clear()