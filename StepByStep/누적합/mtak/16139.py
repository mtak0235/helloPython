import sys
import string
input = sys.stdin.readline
s = input().strip()
q = int(input())
r = [[0 for _ in string.ascii_lowercase[:26]] for __ in range(len(s) + 1)]
for idx, _ in enumerate(s):
    r[idx + 1] = r[idx][:]
    r[idx + 1][ord(_) - ord('a')] += 1
while q:
    q -= 1
    a = input().split()
    print(r[int(a[2]) + 1][ord(a[0]) - ord('a')] - r[int(a[1])][ord(a[0]) - ord('a')])