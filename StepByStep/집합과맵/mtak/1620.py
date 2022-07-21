import sys
input = sys.stdin.readline
n, m = map(int, input().split())
by_name = {input().strip():_ for _ in range(1,n + 1)}
by_id = {v: k for k, v in by_name.items()}
for _ in range(m):
    get = input().strip()
    if get.isdigit():
        print(by_id[int(get)])
    else:
        print(by_name[get])
