import sys

start = 1
cnt = 1
n = int(sys.stdin.readline())

while (n > start):
    start += cnt * 6
    cnt += 1
print(cnt)
