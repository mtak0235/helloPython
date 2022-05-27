# 서로 다른 부분 문자열의 개수

s = input()
answer = 0
tmp = []
for i in range(1, len(s)):
	j = 0
	while (j+i <= len(s)):
		tmp.append(s[j:j+i])
		j += 1
print(len(set(tmp))+1)