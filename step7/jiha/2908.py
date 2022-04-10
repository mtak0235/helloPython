x, y = input().split()
"""
슬라이싱을 활용한 방법
a[start:end:step]
"""
x = x[::-1]
y = y[::-1]

if x > y:
    print(x)
else:
    print(y)