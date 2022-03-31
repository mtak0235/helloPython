import sys

def heapify(li, idx, n):
    l = idx * 2
    r = idx * 2 + 1
    s_idx = idx
    if l <= n and int(li[s_idx][0]) > int(li[l][0]):
        s_idx = l
    if r <= n and int(li[s_idx][0]) > int(li[r][0]):
        s_idx = r
    if l <= n and int(li[s_idx][0]) == int(li[l][0]) and li[s_idx][2] > li[l][2]:
        s_idx = l
    if r <= n and int(li[s_idx][0]) == int(li[r][0]) and li[s_idx][2] > li[r][2]:
        s_idx = r
    if s_idx != idx:
        li[idx], li[s_idx] = li[s_idx], li[idx]
        return heapify(li, s_idx, n)

def heap_sort(v):
    n = len(v)
    v = [0] + v
    for i in range(n, 0, -1):
        heapify(v, i, n)
    for i in range(n, 0, -1):
        print(v[1][0], v[1][1])
        v[i], v[1] = v[1], v[i]
        heapify(v, 1, i - 1)

_cnt = int(sys.stdin.readline())
_list =  [sys.stdin.readline().strip().split() + [_] for _ in range(_cnt)]
heap_sort(_list) 
