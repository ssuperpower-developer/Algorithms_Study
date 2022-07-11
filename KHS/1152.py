a=input()
b=set(a.lower())
c=[0 for i in range(len(b))]
for i in a:
    for j,k in enumerate(b):
        if i.lower()==k:
            c[j]+=1
b=list(b)
d=-1
for i in c:
    if i==max(c):d+=1
if(d): print("?")
else: print(b[c.index(max(c))].upper())