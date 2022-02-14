# 1 ---------------------------------------------
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0 

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] <= m:
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)

# 2 ---------------------------------------------
# from itertools import combinations

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# result = 0

# for cards in combinations(arr, 3):
#     temp_sum = sum(cards)
#     if result < temp_sum <= m:
#         result = temp_sum

# print(result)
