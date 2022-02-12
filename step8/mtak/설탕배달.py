import sys
_sum = int(sys.stdin.readline())
_five = _sum // 5
while (_sum - _five * 5) % 3 != 0 :
    _five -= 1
if _five < 0:
    print(-1)
else:
    print(_five + (_sum - _five * 5) // 3)

