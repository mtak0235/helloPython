s = input()

lst = [-1] * 26
a = ord('a')
for i in range(len(s)):
	if lst[ord(s[i]) - a] == -1:
		lst[ord(s[i]) - a] = i
print(*lst)