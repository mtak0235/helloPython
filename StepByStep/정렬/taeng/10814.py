#
#
#

import sys


if __name__ == "__main__":
    _ = input()
    raw = sys.stdin.readlines()
    result = []
    for i, line in enumerate(raw):
        _age, name = line.strip().split()
        age = int(_age)
        result.append((age, i, name))

    result = sorted(result)
    for age, _, name in result:
        print(age, name)
