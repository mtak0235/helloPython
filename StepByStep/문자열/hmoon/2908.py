import sys

num = list(map(int, sys.stdin.readline().split()))

num1 = list(map(int, str(num[0])))
num2 = list(map(int, str(num[1])))

num1.reverse()
num2.reverse()

num1 = int(''.join(map(str, num1)))
num2 = int(''.join(map(str, num2)))

print(num1 if num1 > num2 else num2)

