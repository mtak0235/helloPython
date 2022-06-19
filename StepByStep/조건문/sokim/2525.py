hour, min = map(int, input().split())
time = int(input())
if (min + time < 60):
	h = hour
	m = min + time
else:
	h = (hour + int(((min + time) / 60))) % 24
	m = (min + time) % 60
print(h, m)
