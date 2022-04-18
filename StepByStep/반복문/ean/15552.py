import sys

f = sys.stdin.read().split('\n')
n = int(f[0])
del f[0]
for i in range(n):
    a, b = f[i].split()
    f[i] = f"{int(a) + int(b)}\n"
sys.stdout.write("".join(f))
