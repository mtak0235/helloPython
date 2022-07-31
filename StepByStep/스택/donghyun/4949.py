lines = open(0).read().strip().split("\n")[:-1]
for line in lines:
	s = []
	for word in line:
		if word in '([':
			s.append(word)
		elif word in ')]':
			if not len(s) or '(['.index(s.pop()) != ')]'.index(word):
				print("no")
				break
	else:
		print("no") if s else print("yes")