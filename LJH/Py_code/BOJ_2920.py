x = list(map(int, input().split()))
if x == sorted(x): print("ascending")
elif x == sorted(x, reverse=True): print("descending")
else : print("mixed")

#x = list(map(int, input().split()))
#[print("ascending") if x == sorted(x) else print("dscending") if x == sorted(x, reverse=True) else print("mixed")]

