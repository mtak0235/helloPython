up, down, height = map(int, input().split())

print((height - up - 1) // (up - down) + 2)