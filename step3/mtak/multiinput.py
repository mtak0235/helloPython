count = int(input())
result = []
while count > 0:
    count -= 1
    [a,b] = input().split()
    result.append(int(a) + int(b))
for p in result:
    print(p)