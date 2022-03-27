import sys

T = int(sys.stdin.readline())

# 이중 for-loop
for i in range(1, T + 1):
    for j in range(0, i):
        if j == i - 1:
            print("*")
        else:
            print("*", end='')

# # 함수로 구분하자 + 스트링+연산
# def printStarline(i):
#     str = ""
#     for i in range(0, i):
#         str += "*"
#     print(str)

# for i in range(0, T):
#     printStarline(i + 1)