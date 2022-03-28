N, M = map(int, input().split())


def pick(limit, lst, count):
    if count == 0:
        print(*lst)
        return
    for i in range(1, limit + 1):
        lst.append(i)
        pick(limit, lst, count - 1)
        lst.pop()


lst = []
pick(N, lst, M)