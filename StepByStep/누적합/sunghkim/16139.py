import sys

S = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())
N = len(S)
DP = [0] * N
for i in range(q):
    a, l, r = list(sys.stdin.readline().split())
    l = int(l); r = int(r)
    DP[0] = 0
    if (a == S[0]):
        DP[0] = 1
    for i in range(1, N):
        if S[i] == a:
            DP[i] = DP[i - 1] + 1
        else:
            DP[i] = DP[i - 1]
    if (l - 1 < 0):
        sys.stdout.write(str(DP[r]) + '\n')
    else:
        sys.stdout.write(str(DP[r] - DP[l - 1]) + '\n')
