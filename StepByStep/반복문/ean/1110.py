import sys

n = int(sys.stdin.readline())
new_num = (n % 10 * 10) + (n // 10 + n % 10) % 10
count = 1

while True:
    if new_num == n:
        print(count)
        break
    new_num = (new_num % 10 * 10) + (new_num // 10 + new_num % 10) % 10
    count += 1
