from collections import deque
import sys

dq = deque()
N,M = map(int,sys.stdin.readline().split())
dq.extend([i for i in range(1,N+1)])

target_list = list(map(int,input().split()))

cnt=0
while target_list:
    right_cnt=0
    left_cnt=0
    
    while target_list[0] != dq[0]:
        dq.rotate(1)
        right_cnt+=1
    dq.rotate(-right_cnt)

    while target_list[0] != dq[0]:
        dq.rotate(-1)
        left_cnt+=1

    if right_cnt < left_cnt:
        dq.rotate(left_cnt+right_cnt)
    cnt+=min(right_cnt, left_cnt)
    dq.remove(target_list[0])
    target_list.pop(0)
   
print(cnt)


'''
1) 리스트 내포
#1  a,b,c,d = [int(x) for x in input().split()]
#2  a,b,c,d = map(int,input().split())
#3  a,b,c,d = [int(x) for x in stdin.readline().rstrip().split()]
stdout.write(str(a*b*c*d))
'''

'''
2) List가 empty인지 확인
list1 = []
list2 = [1,2,3]

if not list1:
    print("list1 is empty")  #list1 is empty
if list2:
    print("list2 is not empty") #list2 is not empty

'''