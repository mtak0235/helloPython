import sys

nums = 0

for i in range(1, int(sys.stdin.readline()) + 1):
    temp = list(map(int, str(i)))
    temp_len = len(temp)
    if (temp_len < 3):
        nums += 1
    elif (temp_len == 3):
        if ((temp[2] - temp[1]) == (temp[1] - temp[0])):
            nums += 1
    elif (temp_len == 4):
        if ((temp[3] - temp[2]) == (temp[2] - temp[1]) == (temp[1] - temp[0])):
            nums += 1
print(nums)
