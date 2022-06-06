import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def find_ans():
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	i_arr = [0 for _ in range(n)]
	i_arr[m] = 1
	cnt = 0
	while True:
		if arr[0] == max(arr):
			cnt += 1
			if i_arr[0] == 1:
				print(cnt)
				break
			arr.pop(0)
			i_arr.pop(0)
		else :
			arr.append(arr[0])
			arr.pop(0)
			i_arr.append(i_arr[0])
			i_arr.pop(0)
	return 

t = int(input())
for _ in range(t):
	find_ans()
