t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    apt = [[1] * (n+1) for i in range(k + 1)]
    for j in range(1, n+1):
        apt[0][j] = j
    for l in range(1, k+1):
        for m in range(2, n+1):
            apt[l][m] = apt[l-1][m] + apt[l][m-1]
    print(apt[k][n])