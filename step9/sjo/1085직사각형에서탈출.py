x, y, w, h = map(int, input().split())

if x > w // 2:
    x_min = w - x
else:
    x_min = x
if y > h // 2:
    y_min = h - y
else:
    y_min = y

print(min(x_min, y_min))