from itertools import combinations
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [0]*(n//2)
ans = 999999999
visited = [False]*(n)
team_list = []
people = [i for i in range(n)]

# def select(k):
# 	if k == n//2:
# 		team_list.append(check)
# 		return
# 	for i in range(n):
# 		if not visited[i]:
# 			check[k] = i
# 			visited[i] = True
# 			select(k+1)
# 			visited[i] = False
# select(0)
for x in combinations(people, n//2):
	team_list.append(x)

for val in team_list:
	t_a = val
	t_b = list(set(people) - set(val))
	val_sum = 0
	for i in t_a:
		for j in t_a:
			val_sum += arr[i][j]
	for i in t_b:
		for j in t_b:
			val_sum -= arr[i][j]
	ans = min(ans, abs(val_sum))

print(ans)