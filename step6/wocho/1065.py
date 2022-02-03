N = int(input())
if N == 1000:
	N -= 1

def is_han(i: int) -> bool:
    return i // 100 - (i // 10) % 10 == (i // 10) % 10 - i % 10

cnt = 99
if N < 100:
    print(N)
else:
    for i in range(100, N + 1):
        if is_han(i):
            cnt += 1
    print(cnt)