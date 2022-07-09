n, *l = open(0).read().strip().split("\n")
s=[]
w1=h1=0
for i, j in map(str.split, l):
	i, j = int(i), int(j)
	s.append(j)
	if i in [1, 2]:
		w1 = max(w1, j)
	else:
		h1 = max(h1, j)
i, j = s.index(w1), s.index(h1)
w2, h2 = abs(s[i-1]-s[(i+1)%6]), abs(s[j-1]-s[(j+1)%6])
print(int(n)*(w1*h1 - w2*h2))