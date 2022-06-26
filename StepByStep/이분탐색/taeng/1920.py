#
#
#

import sys


def bin_search(target, numeric, l, r):
    if l > r:
        return 0

    if l == r:
        if numeric[l] == target:
            return 1
        else:
            return 0

    mid = (l + r) // 2
    if numeric[mid] == target:
        return 1
    elif numeric[mid] > target:
        return bin_search(target, numeric, l, mid)
    else:
        return bin_search(target, numeric, mid + 1, r)


if __name__ == "__main__":
    _ = input()
    numerics = sorted(map(int, sys.stdin.readline().strip().split()))
    _ = input()
    targets = list(map(int, sys.stdin.readline().strip().split()))
    for target in targets:
        print(bin_search(target, numerics, 0, len(numerics) - 1))

