from sys import stdin
n = int(stdin.readline())

# 2차원 배열 만들기, 초기값 설정
arr = [[0]*10 for _ in range(n+1)]
for i in range(1, 10):
	arr[1][i] = 1

# 그림 그려서 이해하는게 직빵
for j in range(2, n+1):
	arr[j][0] = arr[j-1][1]
	arr[j][9] = arr[j-1][8]
	for k in range(1, 9):
		arr[j][k] = (arr[j-1][k-1] + arr[j-1][k+1])%1000000000

print(sum(arr[n])%1000000000)