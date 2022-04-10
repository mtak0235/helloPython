import sys
n = int(sys.stdin.readline())
cnt = [0]*8001
arr = []

for _ in range(n):
	x = int(sys.stdin.readline())
	cnt[x+4000] += 1
	arr.append(x)
print(round(sum(arr)/n))
arr.sort()
print(arr[n//2])

many = []
x = 0
many.append(0)
for i in range(1, 8001):
	if cnt[x] < cnt[i]:
		many.clear()
		many.append(i)
		x = i
	elif cnt[x] == cnt[i]:
		many.append(i)
many.sort()
if len(many) == 1:
	print(many[0] - 4000)
else:
	print(many[1] - 4000)
if n == 1:
	print(0)
else:
	print(arr[-1] - arr[0])