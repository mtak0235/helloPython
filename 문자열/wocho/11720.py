import sys

input = sys.stdin.readline

input()
n = int(input())

cnt = 0
while n > 0:
	cnt += n % 10
	n = n // 10
print(cnt)