import sys
input = sys.stdin.readline

line = input()
ans = []
while line != '.\n':
    memo = []
    for i in range(len(line)):
        flag = True
        if line[i] == '(':
            memo.append('(')
        elif line[i] == '[':
            memo.append('[')
        elif line[i] == ']':
            if memo and memo[-1] == '[':
                memo.pop(-1)
            else:
                flag = False
                break
        elif line[i] == ')':
            if memo and memo[-1] == '(':
                memo.pop(-1)
            else:
                flag = False
                break
    if flag and not memo:
        ans.append('yes')
    else:
        ans.append('no')

    line = input()

print('\n'.join(ans))
