import sys




def heapify(li, idx, n):

    l = idx * 2

    r = idx * 2 + 1

    s_idx = idx

    if l <= n and li[s_idx] > li[l]:

        s_idx = l

    if r <= n and li[s_idx] > li[r]:

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

        print(v[1])

        v[i], v[1] = v[1], v[i]

        heapify(v, 1, i - 1)




_cnt = int(sys.stdin.readline())

_list =  [int(sys.stdin.readline()) for _ in range(_cnt)]

heap_sort(_list) 
