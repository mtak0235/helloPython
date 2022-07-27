s = input().strip()
n = 0
for i, j in enumerate(s.split("-")):
	term = 0
	for k in j.split("+"):
		term += int(k)
	n -= term if i else -term
print(n)