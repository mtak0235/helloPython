def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix

star = ["***", "* *", "***"]
# n = int(input())
# e = 0
# while n != 3:
#     n = n // 3
#     e += 1

# for _ in range(e):
star = get_stars(star)
star = get_stars(star)
for i in star:
    print(i)