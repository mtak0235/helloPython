# 2577

import sys

number = 1
for i in range(0, 3):
	number *= int(sys.stdin.readline())
chkDict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for index, value in enumerate (str(number)):
	if value in chkDict.keys():
		chkDict[value] += 1
for i in chkDict:
	print(chkDict[i])
