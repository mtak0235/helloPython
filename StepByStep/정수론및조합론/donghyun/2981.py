import math
from functools import reduce

l = list(map(int, open(0).read().strip().split("\n")[1:]))
l = [j - l[i - 1] for i, j in enumerate(l)]
n = reduce(lambda x, y: math.gcd(x, y), l)
ans = []
for i in range(2, int(n**.5)+1):
	if not n % i:
		ans.append(i)
		ans.append(n//i)
ans.append(n)
print(*sorted(set(ans)))