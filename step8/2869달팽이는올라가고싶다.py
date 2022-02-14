a, b, v = map(int, input().split())

if (v - b) % (a - b) == 0:
    d = (v - b) // (a - b)
else:
    d = (v - b) // (a - b) + 1

print(d)