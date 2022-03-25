[_hour, _min] = input().split()
_hour = int(_hour)
_min = int(_min)
_min -= 45
if _min < 0:
    _min += 60
    _hour -= 1
if _hour < 0:
    _hour += 24
print(_hour, _min)