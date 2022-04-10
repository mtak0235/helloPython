h, m = map(int, input().split())
t = int(input())

h += t // 60
m += t % 60

h += m // 60
m %= 60
h %= 24

print(h, m)