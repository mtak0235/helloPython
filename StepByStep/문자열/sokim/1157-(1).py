# 입력 받은 문자열을 모두 대문자화 + 리스트화
string = list(input().upper())

# 단어와 등장 횟수를 key-value 쌍으로 저장할 딕셔너리 생성
di = dict()
for i in string :
	di[i] = di.get(i, 0) + 1

# value-key 쌍으로 바꾸어 저장할 리스트 생성
count = list()
for key, value in di.items() :
	new_tuple = (value, key)
	count.append(new_tuple)

# 리스트를 내림차순으로 정렬
count = sorted(count, reverse=True)

# 가장 많이 등장한 단어가 여러 개이면 물음표 출력, 하나라면 해당 단어 출력
if len(count) == 1 :
	print(count[0][1]) 
elif count[0][0] == count[1][0] :
	print('?')
else :
	print(count[0][1])
