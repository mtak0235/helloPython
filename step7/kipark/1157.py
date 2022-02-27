import sys

str = sys.stdin.readline().strip().upper()
arr = [0 for i in range(200)]

for word in str:
	arr[ord(word)] += 1

max_i = 0
max_value = 0
for i in range(0, len(arr)):
	if(arr[i] > max_value):
		max_value = arr[i]
		max_i = i

if(arr.count(max_value) > 1):
	print("?")
else:
	print(chr(max_i))
