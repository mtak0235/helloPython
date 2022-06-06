# 소트인사이드
n = input()
num = []
for i in n:
	num.append(int(i))
num.sort(reverse=True)
result = ""
for i in num:
	result += str(i)
print(int(result))
