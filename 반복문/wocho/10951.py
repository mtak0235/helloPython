import sys

input = sys.stdin.readline

lst = []
while True:
    line = input()
    if not line:
        break
    a, b = map(int, line.split())
    lst.append(str(a + b))
	
print('\n'.join(lst))