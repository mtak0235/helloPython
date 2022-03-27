left = []
right = []

for i in range(3):
    a, b = map(int, input().split())
    left.append(a)
    right.append(b)

for i in range(3):
    count = left.count(left[i])
    if count % 2 == 1:
        x = left[i]

for i in range(3):
    count = right.count(right[i])
    if count % 2 == 1:
        y = right[i]

print(x, y, sep=' ')
