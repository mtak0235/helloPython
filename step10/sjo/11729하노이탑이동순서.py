n = int(input())
print(2**n - 1)

def hanoi(n, a, b):
    if n == 1:
        print(a, b)
        return
    hanoi(n - 1, a, 6 - a - b)
    hanoi(1, a, b)
    hanoi(n - 1, 6 - a - b, b)

hanoi(n, 1, 3)