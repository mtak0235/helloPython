# 1 ---------------------------------------------
# n = int(input())

# result = 1

# while (n > 1):
#     result *= n
#     n -= 1

# print(result)

# 2 ---------------------------------------------
def factorial(x):
    result = 1
    if x > 0:
        result = x * factorial(x - 1)
    return result

n = int(input())
print(factorial(n))