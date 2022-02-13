# 한 천재의 도움으로 쉽게 풀었읍니다
t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    back = (n // h) + 1
    if (n % h) == 0:
        front = h
        back -= 1
    else:
        front = n % h
    print(100*front + back)