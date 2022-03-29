N, X = map(int, input().split())
A = list(map(input().split()))
for i in range(N):
    if X>A[i]:
        print("%d" %A[i], end=" ")