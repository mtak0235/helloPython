import sys
import array as arr

nums = arr.array('i', [0] * 42)
for i in range(10):
    nums[int(sys.stdin.readline()) % 42] += 1
print(42 - nums.count(0))
