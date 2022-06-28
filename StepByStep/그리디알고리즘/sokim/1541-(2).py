import sys

# 입력 받은 수식을 '-' 기준으로 파싱(예: '55-50+40' -> '55', '50+40')
parenthesis = sys.stdin.readline().strip().split('-')

# 각 괄호 안의 숫자들을 합한 값을 담을 리스트 (예: '55', '90')
add = list()
for i in parenthesis :
	# 괄호 안의 숫자들을 다시 '+' 기준으로 파싱 (예: '50+40' -> '50', '40')
	nums = i.split('+')
	# 괄호 안의 숫자들을 모두 더한 값
	sum = 0
	for num in nums :
		sum += int(num)
	add.append(sum)

# 괄호를 삽입한 후의 수식 계산 결과 (예: 55-(50+40))
total = add[0]
for i in range(1, len(add)) :
	total -= add[i]
print(total)
