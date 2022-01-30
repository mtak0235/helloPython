def cnt(n):
    count = 0
    if n == 1000:
        n -= 1
    for i in range(100, n+1):
        n1 = i // 100
        n2 = (i // 10) % 10
        n3 = i % 10
        if (n1 - n2) == (n2 - n3):
            count += 1
    return count

n = int(input())
count = 0
if n > 99:
    count = cnt(n) + 99
else:
    count = n
print(count)