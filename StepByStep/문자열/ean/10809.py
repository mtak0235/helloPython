import sys

line = sys.stdin.readline().rstrip()
l = [-1] * 26
for i, v in enumerate(line):
    c_index = ord(v) - ord('a')
    if l[c_index] == -1:
        l[c_index] = i

for i in l:
    print(i, end=' ')
