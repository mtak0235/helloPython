#
#
#

import sys


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    rank = {v: i for i, v in enumerate(sorted(set(arr)))}
    result = [str(rank[v]) for v in arr]
    print(" ".join(result))