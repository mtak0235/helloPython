num = int(input())

next = (num % 10) * 10 + (num // 10 + num % 10) % 10

cnt = 1
while next != num:
    next = (next % 10) * 10 + (next // 10 + next % 10) % 10
    cnt += 1
    
print(cnt)