#
#
#


import sys


if __name__ == "__main__":
    _ = input()
    sorted_nums = sorted([int(line.strip()) for line in sys.stdin.readlines()])
    count_value = {}
    max_count = 0
    for num in sorted_nums:
        if num not in count_value:
            count_value[num] = 0
        count_value[num] += 1
        if max_count < count_value[num]:
            max_count = count_value[num]
    max_nums = []
    for num, v in count_value.items():
        if v == max_count:
            max_nums.append(num)

    print(round(sum(sorted_nums) / len(sorted_nums)))
    print(sorted_nums[len(sorted_nums) // 2])
    if len(max_nums) == 1:
        print(max_nums[0])
    else:
        print(sorted(max_nums)[1])
    print(sorted_nums[-1] - sorted_nums[0])
