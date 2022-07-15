#
#
#

import sys

if __name__ == "__main__":
    _ = input()
    nums = [int(line.strip()) for line in sys.stdin.readlines()]
    stack = []
    for num in nums:
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))