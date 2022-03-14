a,b = map(int, input().split())
c = int(input())

a = (a + (b + c) // 60) % 24
b = (b + c) % 60

print(a, b)
