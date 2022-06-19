import sys

def main():
	x, y = map(int, input().split())
	if x > y:
		print('>')
	elif x < y:
		print('<')
	else:
		print('==')

if __name__ == '__main__':
	main()
