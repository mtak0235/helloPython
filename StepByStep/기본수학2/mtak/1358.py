from cmath import sqrt
import sys
import math
input = sys.stdin.readline
W, H, X, Y, P = map(int, input().split())
ppl = []
def is_in_circle(p):
    dis1 = math.sqrt(math.pow(p[0] - X, 2) + math.pow(p[1] - (Y + H//2), 2))
    dis2 = math.sqrt(math.pow(p[0] - (X + W), 2) + math.pow(p[1] - (Y + H//2), 2))
    return 1 if min(dis1, dis2) <= H//2 else 0

def is_in_field(p):
    if not (X - H//2 <= p[0] <= X + W + H//2) or not (Y <= p[1] <= Y + H):
        return 0
    if X<p[0]<X + W:
        return 1
    if not is_in_circle(p):
        return 0
    return 1


for _ in range(P):
    ppl.append(list(map(int, input().split())))
cnt = 0
for p in ppl:
    cnt += is_in_field(p);
print(cnt)