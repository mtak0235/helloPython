# 잃어버린 괄호
# 그리디 알고리즘

import sys

nums = sys.stdin.readline().split('-')
answer = sum(list(map(int, nums[0].split('+'))))
for i in range(1, len(nums)):
    answer -= sum(list(map(int, nums[i].split('+'))))

print(answer)