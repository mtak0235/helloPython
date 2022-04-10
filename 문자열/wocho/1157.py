s = input().lower()

lst = [0] * 26
a = ord('a')
for i in range(len(s)):
	idx = ord(s[i]) - a
	lst[idx] += 1

max_idx = 0
dup = False
for i in range(1, 26):
	if lst[i] > lst[max_idx]:
		max_idx = i
		dup = False
	elif lst[i] == lst[max_idx]:
		dup = True

print('?' if dup else chr(max_idx + ord('A')))