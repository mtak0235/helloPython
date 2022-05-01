# 통계학
from collections import Counter

n = int(input())
num_list = []
for _ in range(n):
	num_list.append(int(input()))
# 산술평균
print(round(sum(num_list) / n))
# 중앙값
num_list.sort()
print(num_list[n//2])
# 최빈값
cnt = Counter(num_list)
mode = cnt.most_common()
if len(num_list) > 1:
	if mode[0][1] == mode[1][1]:
		print(mode[1][0])
	else:
		print(mode[0][0])
else:
	print(num_list[0])
# 범위
print(num_list[-1] - num_list[0])
