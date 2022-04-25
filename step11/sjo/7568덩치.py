n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')