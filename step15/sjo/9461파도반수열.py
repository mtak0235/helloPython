t = int(input())
d = [0] * 101
d[1], d[2], d[3] = 1, 1, 1
d[4] = 2

def f(x):
    if d[x] != 0:
        return d[x]
    else:
        for i in range(5, x + 1):
            d[x] = f(x - 3) + f(x - 2)
            return d[x]

for _ in range(t):
    print(f(int(input())))