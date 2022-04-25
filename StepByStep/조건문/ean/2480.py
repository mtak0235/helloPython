import sys

x, y, z = map(int, sys.stdin.readline().split())
reward = 1000
multiplier = 100
num = max(x, y, z)
if x == y and y == z:
    reward = 10000
    multiplier = 1000
elif x == y:
    num = x
elif y == z:
    num = y
elif z == x:
    num = z
else:
    reward = 0
print(reward + num * multiplier)
