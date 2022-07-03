# () 을 리스트에 삽입
def	insert_parenthesis(i, expression) :
	expression.insert(i, '(')
	for j in range(i + 1, len(expression)) :
		if expression[j] == '-' :
			expression.insert(j, ')')
			return j + 1
	expression.append(')')
	return j + 1

# 입력 받은 수식을 리스트화
expression = list(input())
# 다음 '-'의 위치
pos = 0
for i in range(len(expression)) :
	# 다음 '-'의 위치가 나오기 전까지는 스킵
	if i < pos :
		continue
	elif expression[i] == '-' :
		pos = insert_parenthesis(i + 1, expression)

# 수식 리스트를 문자열화
string = ''
for i in expression :
	string += str(i)
# 문자열을 파싱하여 계산
sum = eval(string)
print(sum)
