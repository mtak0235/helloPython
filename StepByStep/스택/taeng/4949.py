#
#
#

import sys


if __name__ == "__main__":
    while True:
        line = sys.stdin.readline().rstrip()
        if line == ".":
            break
        stack = []
        for c in line:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if len(stack) == 0:
                    stack.append(1)
                    break
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
            elif c == "[":
                stack.append(c)
            elif c == "]":
                if len(stack) == 0:
                    stack.append(1)
                    break
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append("]")
            elif c == '.':
                break
        if len(stack):
            print("no")
        else:
            print("yes")
