# 1    2~7   8~19   20~37
#   +6개   +12개   +18개    

def	get_result(num) :
	i = 0
	hive_prev = 1
	hive_now = 1
	while True:
		hive_now = hive_prev + 6 * i
		if num <= hive_now :
			return i + 1
		else:
			hive_prev = hive_now
			i += 1

num = int(input())
result = get_result(num)
print(result)
