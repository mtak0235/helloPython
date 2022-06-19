first = int(input())

cycle = 0
# new = 10a + b
new = first
while True:
	# new = int(str(b) + str((a + b)%10))
	new = int(str(new % 10) + str((new // 10 + new % 10) % 10))
	cycle += 1
	if new == first:
		break
print(cycle)
