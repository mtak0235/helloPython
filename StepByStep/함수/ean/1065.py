import sys

def check(n):
    diff = n // 10 % 10 - n % 10
    n //= 10
    while n > 9:
        if (n % 10 + diff) != (n // 10 % 10):
            return False
        n //= 10
    return True

n = int(sys.stdin.readline())
count = 0
for i in range(1, n + 1):
    if check(i):
        count += 1
print(count)
