def	 get_break_even_point(A, B, C) :
	if B >= C :
		return -1
	else :
		return (A // (C-B) + 1)

# 고정비용, 가변비용, 판매가격
A, B, C = map(int, input().split())

result = get_break_even_point(A, B, C)
print(result)
