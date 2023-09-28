x,y,w,h = map(int, input().split())

w-=x
h-=y
if(w>=x):
    w=x
if(h>=y):
    h=y
print(min(w,h))