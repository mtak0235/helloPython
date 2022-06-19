import sys

remain = []

while (1):
	try:
		remain.append((int(sys.stdin.readline()) % 42))
	except:
		break

remain = set(remain)
print(len(list(remain)))
