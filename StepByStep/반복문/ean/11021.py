import sys

for i in range(int(sys.stdin.readline())):
    a, b = sys.stdin.readline().split()
    sys.stdout.write(f"Case #{i+1}: {int(a) + int(b)}\n")
