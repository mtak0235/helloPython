import sys
input = sys.stdin.readline
cnt = int(input())
a = [int(input()) for _ in range(cnt)]
s = list()
toP = list()
p = 1
for num in a:
    while p <= num:
        s.append(p)
        toP.append("+")
        p += 1
    if s[-1] == num:
        s.pop()
        toP.append("-")
    else:
        print("NO")
        exit()
for i in toP:
    print(i)