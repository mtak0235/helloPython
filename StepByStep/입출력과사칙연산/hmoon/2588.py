import sys

if __name__ == '__main__':
    x = input("")
    y = input("")
    for i in range(2, -1, -1):
        print(int(y[i]) * int(x))
    print(int(y) * int(x))
