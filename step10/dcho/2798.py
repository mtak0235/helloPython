# 2798

import sys

n, m = map(int,sys.stdin.readline().split(' '));

cardNumber: list = [x for x in map(int,sys.stdin.readline().split(' '))];
result: int = 0;
for i in cardNumber:
	for j in cardNumber:
		for k in cardNumber:
			if i != j and i != k and j != k:
				sum: int = i + j + k;
				if sum > result and sum <= m:
					result = sum;
print(result);
