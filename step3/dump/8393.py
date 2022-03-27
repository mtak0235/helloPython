import sys

n = int(sys.stdin.readline())

# 삼각수 응용
print(int(n * (n + 1) / 2))

# # for-range 반복문
# def get_sum_to_n(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum
# print(get_sum_to_n(n))
