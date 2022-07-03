string = input()

# 알파벳(a~z)를 담을 리스트
alphabets = list()
# a와 z의 아스키코드 알아내기
a_ascii = ord('a')
z_ascii = ord('z')
for i in range(a_ascii, z_ascii + 1) :
	alphabets.append(chr(i))

# 알파벳 순서대로 입력 받은 문자열 내에 존재하는지 검사
for i in alphabets :
	print(string.find(i), end='')
	if i != 'z' :
		print(' ', end='')
