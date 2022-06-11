hour, min = input().split()
hour = int(hour)
min = int(min)
if (min >= 45):
	min = min - 45
else:
	min = (min + 15) % 60
	hour = (hour + 23) % 24
print(hour, min)
