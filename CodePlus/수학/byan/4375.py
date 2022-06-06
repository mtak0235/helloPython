import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

while True:
	# input이 없다면 break
	try:
		n = int(input())
	except:
		break 
	num = 0
	i = 1
	while True:
		num = num * 10 + 1
		num %= n
		if num == 0:
			print(i)
			break
		i+=1