#
#
#


import sys


if __name__ == "__main__":
    input()
    arr = sorted([list(reversed(list(map(int, line.strip().split())))) for line in sys.stdin.readlines()])
    arr2 = [f"{b} {a}" for a, b in arr]
    print("\n".join(arr2))
