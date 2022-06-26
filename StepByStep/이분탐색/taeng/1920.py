#
#
#

import sys


if __name__ == "__main__":
    _ = input()
    numerics = set(sys.stdin.readline().strip().split())
    _ = input()
    targets = ["1" if n in numerics else "0" for n in sys.stdin.readline().strip().split()]
    print("\n".join(targets))
