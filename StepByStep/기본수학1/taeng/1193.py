# https://www.acmicpc.net/problem/1193
# 분수찾기
#

def pattern(_X, _band):
	while True:
		if _X - _band <= 0:
			band_mid = (_band // 2) + 1
			if _X <= band_mid:
				return (_X)
			else:
				return (2 * band_mid - _X)
		_X -= _band
		_band += 4


if __name__ == "__main__":
	X = int(input())
	x, y = pattern(X, 1), pattern(X, 3)
	print(f"{x}/{y}")