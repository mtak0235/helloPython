import sys
input = sys.stdin.readline

N = int(input())

ans = []
for _ in range(N):
    flag = True
    stack = []
    brackets = input().strip()
    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.append(True)
        else:
            if not stack:
                ans.append('NO')
                flag = not flag
                break
            else:
                stack.pop(-1)
    if flag and not stack:
        ans.append('YES')
    elif flag:
        ans.append('NO')


print('\n'.join(ans))
