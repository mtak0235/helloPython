ans = [0]*10001

def d(n):
    count = n
    while n >= 10:
        count += n % 10
        n = n // 10
    count += n
    return count

for i in range(1, 10001):
    h = d(i)
    if h < 10001:
        ans[h] = 1

for j in range(1, 10001):
    if ans[j] == 0:
        print(j)