# 나눗셈 만세
a, b, c = map(int, input().split())

cnt = 0
if b >= c:
    print(-1)
else:
    cnt = a//(c-b) + 1
    print(cnt)