import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    start = 1
    cnt = 1
    while (n > start):
        start = start + cnt + 1
        cnt += 1
    index = (cnt * (cnt + 1)) / 2
    diff = index - n
    a, b = cnt - diff, 1 + diff
    if cnt % 2 == 0:
        print(f'{int(a)}/{int(b)}')
    else:
        print(f'{int(b)}/{int(a)}')
