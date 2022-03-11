N = int(input())

lst = [0] * N
memo = [False] * N
count = 0


def check(x):
    for i in range(x):
        if x - i == abs(lst[x] - lst[i]):
            return False
    return Tru -

def pick(cnt):
    global count
    if cnt == N:
        count += 1
        return
    for i in range(N):
        if memo[i]:
            continue
        lst[cnt] = i
        if check(cnt):
            memo[i] = True
            pick(cnt + 1)
            memo[i] = False


pick(0)
print(count)
