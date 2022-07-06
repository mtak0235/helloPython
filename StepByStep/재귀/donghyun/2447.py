import sys

input = sys.stdin.readline
num = int(input())
def star(n):
    if n == 3:
        return
    l = star.l
    star.l = []
    for i in l:
        star.l.append(i * 3)
    for i in l:
        star.l.append(i + ' ' * len(i) + i)
    for i in l:
        star.l.append(i * 3)
    star(n//3)
star.l = ["***", "* *", "***"]
star(num)
print("\n".join(star.l))