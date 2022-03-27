import sys
n = int(sys.stdin.readline())
arr = [0]*n
visited = [0]*n
cnt = 0
def veri(x) -> bool:
	for i in range(x):
		if arr[x] - arr[i] == 0 or abs(arr[x] - arr[i]) == x - i:
			return False
	return True

def func(k):
	global cnt
	if k == n:
		cnt += 1
	else:
		for j in range(n):
#			if visited[j] == 1:
#				continue
			arr[k] = j
			if veri(k):
#				visited[j] = 1
				func(k+1)
#				visited[j] = 0
func(0)
print(cnt)
### visited존재가 시간복잡도에 어떻게 영향을 주는지 고민