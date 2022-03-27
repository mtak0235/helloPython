import sys
_input = sys.stdin.readline().strip()
a = {}
for i in range(len(_input)):
    if _input[i] in a:
        continue
    a[_input[i]] = i
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in a:
        print(a[chr(i)], end = " ")
    else:
        print(-1, end = " ")
