data = list(map(int,input().split()))
list_a=[n for n in range(1,9)]

if data==list_a:
    print("ascending")
elif data==list(reversed(list_a)):
    print("descending")
else:
    print("mixed")