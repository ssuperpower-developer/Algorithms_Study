from collections import deque
a=deque()

for i in range(1,11):
    a.append(i)

def Number3():
    a.appendleft(a.pop())
Number3()
print(a)