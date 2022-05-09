# 약수
n = int(input())
num = list(map(int, input().split()))
num.sort()
answer = num[0] * num[-1]
print(answer)