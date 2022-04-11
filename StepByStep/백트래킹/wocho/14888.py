N = int(input())

nums = list(map(int, input().split()))
operators = list(map(int, input().split()))

maxv = float("-inf")
minv = float("inf")

def calculate(operand, idx):
    if idx == N:
        global maxv;
        global minv;
        maxv = max(maxv, operand)
        minv = min(minv, operand)
    for i in range(4):
        if operators[i]:
            operators[i] -= 1
            if i == 0:
                calculate(operand + nums[idx], idx + 1)
            elif i == 1:
                calculate(operand - nums[idx], idx + 1)
            elif i == 2:
                calculate(operand * nums[idx], idx + 1)
            else:
                if operand < 0:
                    calculate((abs(operand) // nums[idx]) * -1, idx + 1)
                else:
                    calculate(operand // nums[idx], idx + 1)
            operators[i] += 1

calculate(nums[0], 1)

print(maxv)
print(minv)
