# 1712 (아니 커밋 메세지 왜이래)
# 손익분기점
# 기본 수학 1


if __name__ == "__main__":
	A, B, C = map(int, input().split())
	if A > 0 and B >= C:
		print(-1)
		exit(0)
	margin = C - B
	ret = A // margin + 1
	print(ret)
