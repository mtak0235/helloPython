#[4153] step9, 직각삼각형 kipark
import sys

while(1):
	abc = list(map(int, input().split()))
	if sum(abc) == 0:
		break
	c = max(abc)
	abc.remove(c)
	result = "right" if (abc[0]**2) + (abc[1]**2) == (c**2) else "wrong"
	print(result)