hour, min = input().split()
hour = int(hour)
min = int(min)
if (min >= 45):
	min = min - 45
elif (min < 45 and hour != 0):
	min += 15
	hour -= 1
else:
	min += 15
	hour = 23
print(hour, min)
