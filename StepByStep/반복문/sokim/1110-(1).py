def add_zero(string):
	new_string = string
	if len(string) == 1:
		new_string = "0" + string
	return new_string

def get_new_num(num, cnt):
	tens = int(num[0])
	units = int(num[1])
	add_num = str(tens + units)
	add_num = add_zero(add_num)

	new_num = str(units) + add_num[1]
	new_num = add_zero(new_num)
	cnt[0] += 1
	return new_num

cnt = [0]
input_num = add_zero(input())
prev_num = input_num

while True:
	prev_num = add_zero(prev_num)
	new_num = get_new_num(prev_num, cnt)
	if new_num == input_num:
		break
	else:
		prev_num = new_num
print(cnt[0])
