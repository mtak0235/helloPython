_year = int(input())
_is_leap = 0
if ((_year % 4 == 0) & (_year % 100 != 0)) | (_year % 400 == 0):
    _is_leap = 1
print(_is_leap)