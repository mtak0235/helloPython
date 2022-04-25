h, m = map(int, input().split())

if m < 45:
    m += 15
    if h == 0:
        h = 23
    else:
        h -= 1
else:
    m -= 45
print("{0} {1}".format(h, m))