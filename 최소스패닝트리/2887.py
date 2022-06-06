import sys

n = int(input())
node = []
planet = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    planet.append([x, y, z, i])

for i in range(3):
    planet.sort(key=lambda x:x[i])
    for j in range(1, n):
        node.append([planet[j][3], planet[j - 1][3], abs(planet[j][i] - planet[j - 1][i])])

parent = [i for i in range(n + 1)]
cost = 0
node.sort(key=lambda x:x[2])

def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return parent[x]

for a, b, c in node:
    A = find_parent(a)
    B = find_parent(b)
    if A != B:
        if A > B:
            parent[A] = B
        else:
            parent[B] = A
        cost += c
print(cost)
