import sys
#### 값 접근할때는 딕셔너리 사용
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr1 = sorted(list(set(arr)))
dic = {arr1[i] : i for i in range(len(arr1))}
for j in arr:
	print(dic[j], end=' ')