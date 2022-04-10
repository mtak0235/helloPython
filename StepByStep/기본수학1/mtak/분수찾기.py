import sys
_turn = 0 
_denominator = 1
_numerator = 1
flag = 0
_input = int(sys.stdin.readline())
while _denominator:
    if _denominator % 2 == 0:
        for _numerator in range(1, _denominator + 1):
            _turn += 1
            if _turn == _input:
                flag += 1
                break
    else:
        for _numerator in range(_denominator, 0, -1):
            _turn += 1
            if _turn == _input:
                flag += 1
                break
    if flag == 1:
        break
    _denominator += 1
print(f"{_numerator}/{_denominator+ 1 - _numerator}")
