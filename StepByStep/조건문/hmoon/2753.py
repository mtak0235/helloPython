import sys

# 윤년 1 아니면 0
# 윤년은 연도가 4의 배수 100의 배수가 아닐때 또는 400의 배수
# 윤년 == year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    year = int(input())
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()
