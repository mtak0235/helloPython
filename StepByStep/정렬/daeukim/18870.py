# 좌표 압축
n = int(input())
num = list(map(int, input().split()))
num2 = list(sorted(set(num)))
dic = {num2[i] : i for i in range(len(num2))
}
for i in num:
	print(dic[i], end=' ')