x, y = map(int, input().split())
z = int(input())
y = y + z
x = x + y//60
y = y%60
x = x%24
print(x, y, sep=' ')