import sys

def main():
	x = int(input())
	if x >= 90 and x <= 100:
		print('A')
	elif x >= 80 and x <= 89:
		print('B')
	elif x >= 70 and x <= 79:
		print('C')
	elif x >= 60 and x <= 69:
		print('D')
	else:
		print('F')

if __name__ == '__main__':
	main()
