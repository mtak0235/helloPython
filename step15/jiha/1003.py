n = int(input())

#0과 1의 갯수를 따로 저장
cnt0 = [1, 0]
cnt1 = [0, 1]

for i in range(2, 41):
	cnt0.append(cnt0[i-2] + cnt0[i-1])
	cnt1.append(cnt1[i-2] + cnt1[i-1])
for _ in range(n):
	val = int(input())
	print(cnt0[val], cnt1[val])