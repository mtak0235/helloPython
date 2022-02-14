import sys

board_a = set(range(1, 10001))
board_b = set()

sys.setrecursionlimit(100000)
def check(a: int):
	if(a > 10000):
		return 0
	result = a
	for i in range(len(str(a))):
		result += int(str(a)[i])
	board_b.add(result)
	check(a + 1)

if __name__ == '__main__':
	check(1)
	
	for i in sorted(board_a - board_b):
		print(i)
