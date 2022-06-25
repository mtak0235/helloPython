import sys

if __name__ == "__main__":
    fixed_cost, variable_cost, price = map(int, sys.stdin.readline().strip().split())
    if variable_cost >= price:
        print(-1)
    else:
        print(int(fixed_cost // (price - variable_cost) + 1))
