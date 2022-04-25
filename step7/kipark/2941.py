import sys

arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = sys.stdin.readline().strip()

# result = 0 

for i in arr:
	# result += str.count(i)  틀리는 테스트 케이스 있음
	str = str.replace(i, '')

print(len(str))
