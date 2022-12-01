x, y, w, h = map(int, input().split())
print(min(x-0, y-0, w-x, h-y))
#사각형의 네 모서리 중 가장 가까운데로 가면 된다.