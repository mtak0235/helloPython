n = int(input())

ans = 1
if (n -2) > -1:
    l = (n-2) // 6
    s = -1
    for i in range(1, n):
        s += i
        if s >= l:
            ans += i
            break
print(ans)