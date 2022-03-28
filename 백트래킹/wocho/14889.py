import sys
input = sys.stdin.readline

N = int(input())

mat = []
for _ in range(N):
    mat.append(list(map(int, input().split())))

check = [False] * N

ans = float("inf")


def recur(idx, cnt):
    if idx >= N:
        return
    if cnt == N // 2:
        a = b = 0
        A = []
        B = []
        for i in range(N):
            if check[i]:
                A.append(i)
            else:
                B.append(i)
        for i in range(N // 2):
            for j in range(N // 2):
                if i == j:
                    continue
                a += mat[A[i]][A[j]]
                b += mat[B[i]][B[j]]
        global ans
        ans = min(ans, abs(b - a))
        return
    for i in range(idx, N):
        check[i] = True
        recur(i + 1, cnt + 1)
        check[i] = False


recur(0, 0)
print(ans)
