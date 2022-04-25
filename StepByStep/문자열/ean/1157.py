import sys

S = sys.stdin.readline().rstrip().upper()
l = [0] * 26
for c in S:
    l[ord(c) - ord('A')] += 1
M = max(l)
if l.count(M) > 1:
    print('?')
else:
    print(chr(ord('A') + l.index(M)))
