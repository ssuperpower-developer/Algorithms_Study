import sys
input=sys.stdin.readline
N,M=map(int,input().split())
a=list(map(int,input().split()))
sum=0
min=1
max=max(a)
mid=(min+max)//2

while min<=max:
    sum=0
    for i in a:
        if i-mid>=0:
            sum+=i-mid
    if sum==M:
        break
    elif sum>M:
        min=mid+1
    elif sum<M:
        max=mid-1
    mid=(min+max)//2
print(mid)


# def binarySearch(after,number):
#     first=0
#     last=number-1
#     while(first<=last):
#         mid=(first+last)//2
#         if after==beforelist[mid]:
#             return 1
#         elif after> beforelist[mid]:
#             first=mid+1
#         elif after< beforelist[mid]:                
#             last=mid-1
#     return 0