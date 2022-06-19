import sys

def main():
    num = list(map(int, input().split()))
    for i in range(1, 7):
        cnt = num.count(i)
        if cnt == 3:
            print(100**2 + (i * (10**3)))
            return
        elif cnt == 2:
            print(10**3 + (i * (10**2)))
            return
    print(max(num) * (10**2))
    return

if __name__ == '__main__':
    main()
