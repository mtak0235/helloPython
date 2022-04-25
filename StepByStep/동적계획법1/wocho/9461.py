import sys
input = sys.stdin.readline

T = int(input())
memo = [0, 1, 1, 1, 2, 2]

ans = []
for _ in range(T):
    target = int(input())
    for i in range(len(memo), target + 1):
        memo.append(memo[i - 1] + memo[i - 5])
    ans.append(str(memo[target]))

print('\n'.join(ans))
