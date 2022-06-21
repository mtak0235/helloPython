# 가장 가까운 공통 조상
# 유니온 파인드, 트리

import sys

inp = sys.stdin.readline

T = int(inp())

for _ in range(T):
    N = int(inp())
    par = [-1] * (N + 1)
    node1_par = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = map(int, inp().split())
        par[B] = A

    node1, node2 = map(int, inp().split())
    
    # node1의 모든 부모 체크
    while node1 > -1:
        node1_par[node1] = 1
        node1 = par[node1]

    answer = -1
    while True:
        if node1_par[node2] :
            answer = node2
            break
        node2 = par[node2]

    print(answer)