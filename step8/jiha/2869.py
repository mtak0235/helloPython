a, b, v = map(int, input().split())

day = (v - a) // (a - b) + 1
if (v - a) % (a - b) != 0:
    day += 1

print(day)