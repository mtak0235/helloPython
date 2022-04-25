t = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def f(x):
    if x >= len(zero):
        for i in range(len(zero), x + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2] + one[i - 1])
    print(zero[x], one[x])

for _ in range(t):
    num = int(input())
    f(num)
        
