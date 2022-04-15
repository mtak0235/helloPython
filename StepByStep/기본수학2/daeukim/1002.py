# 터렛
import math

t = int(input())
for _ in range(t):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
	if d==0 and r1==r2:
		print(-1) # 동심원인 경우
	elif abs(r1-r2) == d or r1 + r2 == d:
		print(1) # 외접 또는 내접
	elif abs(r1-r2) < d < (r1+r2):
		print(2)
	else:
		print(0)# 만나지 않는 경우
