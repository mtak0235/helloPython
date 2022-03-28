N = int(input())

lst = []
while N:
    lst.append(N % 10)
    N //= 10

lst.sort()
answer = 0
for i in range(len(lst)):
    answer += lst[i] * (10 ** i)
print(answer)