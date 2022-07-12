import sys

def solve(n, stars):
    if (n == 3):
        return (stars)
    temp = []
    for i in stars:
        temp.append(i * 3)
    for i in stars:
        temp.append(i +' ' * len(stars) + i)
    for i in stars:
        temp.append(i * 3)
    return (solve(n // 3, temp))

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = ["***", "* *", "***"]
    print("\n".join(solve(n, arr)))
