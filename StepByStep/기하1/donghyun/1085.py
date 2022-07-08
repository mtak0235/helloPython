x, y, w, h = map(int, open(0).read().split())
print(min(x, y, w-x, h-y))