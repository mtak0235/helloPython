import sys
input = sys.stdin.readline

N = int(input())

cur = 0
ans = []
stack = []
flag = True
for _ in range(N):
    num = int(input())
    if num > cur:
        for i in range(cur + 1, num):
            stack.append(i)
            ans.append('+')
        ans.append('+')
        ans.append('-')
        cur = num
    else:
        if stack:
            if num == stack.pop():
                ans.append('-')
            else:
                flag = False
                break
        else:
            flag = False
            break
if not flag:
    print('NO')
else:
    print('\n'.join(ans))
