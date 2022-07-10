# 10250
# ACM 호텔
# 기본 수학 1


if __name__ == "__main__":
	TC = int(input())
	for tc in range(TC):
		H, W, N = map(int, input().split())
		N -= 1
		Y, X = N % H, N // H
		print(f"{Y + 1}{str(X + 1).zfill(2)}")
