n = int(input())
d = 1
cnt = 1

while n > d:
    d += cnt * 6
    cnt += 1

print(cnt)