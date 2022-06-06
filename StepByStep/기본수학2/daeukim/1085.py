# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
x_dif = min(w-x, x)
y_dif = min(h-y, y)
print(min(x_dif, y_dif))