import sys

year = int(sys.stdin.readline())

# 삼항연산자, 함수 구조 활용
def isLeafYear(year):
    return True if year % 400 == 0 else True if year % 4 == 0 and year % 100 != 0 else False
print(1) if isLeafYear(year) else print(0)

# # 조건문
# if year % 400 == 0:
#     print(1)
# elif year % 4 == 0 and year % 100 != 0:
#     print(1)
# else:
#     print(0)