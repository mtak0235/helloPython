#
#
#

if __name__ == "__main__":
    N = int(input())
    for n in range(N):
        line = input()
        if len(line) % 2 == 1:
            print("NO")
            continue
        stack = []
        for c in line:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    stack.append(1)
                    break
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")
        if len(stack):
            print("NO")
        else:
            print("YES")
