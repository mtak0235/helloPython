N, M = map(int, input().split())


def pick(start, limit, lst, count):
    if count == 0:
        print(*lst)
        return
    for i in range(start, limit + 1):
        lst.append(i)
        pick(i, limit, lst, count - 1)
        lst.pop()


lst = []
pick(1, N, lst, M)