import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = []
no = True
count = 1

for i in arr:
	while count <= i:
		stack.append(count)
		ans.append("+")
		count += 1
	if stack[-1] == i:
		stack.pop()
		ans.append("-")
	else :
		no = False
if (no == False):
	print("NO")
else:
	for i in ans:
		print(i)
