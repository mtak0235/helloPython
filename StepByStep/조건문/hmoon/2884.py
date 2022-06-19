import sys

def	main():
    x, y = map(int, input().split())
    if y < 45:
        if x == 0:
            x = 23
        else:
            x -= 1
        y = abs(60 - (45 - y))
    else:
        y -= 45
    print(x, y)

if __name__ == '__main__':
    main()
