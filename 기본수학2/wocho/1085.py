x, y, w, h = map(int, input().split())

dx = min(x, w - x)
dy = min(y, h - y)
print(min(dx, dy))