# 좌표 정렬하기
n = int(input())
m = []
for _ in range(n):
	m.append(list(map(int, input().split())))
m.sort()
for i in m:
	print(i[0], i[1])