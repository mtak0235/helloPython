arr = list(map(int, input()))
cnt = [0] * 10

for i in arr:
    cnt[i] += 1

for i in range(9, -1, -1):
    for _ in range(cnt[i]):
        print(i, end='')