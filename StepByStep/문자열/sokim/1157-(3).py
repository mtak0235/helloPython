a = input().upper()
di = {x : 0 for x in a}
result = list()
for i in a :
	di[i] += 1
for letter, cnt in di.items() :
	if cnt == max(di.values()) :
		result.append(letter)
if len(result) == 1 :
	print(result[0])
else :
	print('?')
