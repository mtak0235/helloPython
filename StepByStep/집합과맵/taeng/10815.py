#
#
#

import sys


_, nset, __ = input(), set([n for n in sys.stdin.readline().strip().split()]), input()
print(" ".join(["1" if m in nset else "0" for m in sys.stdin.readline().strip().split()]))
