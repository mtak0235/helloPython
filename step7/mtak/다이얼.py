import sys
_input = sys.stdin.readline()
_alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".upper().split()
_dial_lst = [_alphabet[0:3], _alphabet[3:6], _alphabet[6:9], _alphabet[9:12], _alphabet[12:15], _alphabet[15:19], _alphabet[19:22], _alphabet[22:26]]
_ret = 0
for c in _input:
	for i, chunk in enumerate(_dial_lst):
		if c in chunk:
			_ret += (i + 3)
print(_ret)
