import sys

words = input()

arr = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
result = 0

for i in words:
	result += arr[ord(i)-ord('A')] + 1
print(result)