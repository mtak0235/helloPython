import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))


def compare(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        elif a[0] == b[0]:
            return 0
        else:
            return 1
    else:
        return 1


def merge_sort(lst):
    def sort(start, end):
        if end - start < 2:
            return
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        merge(start, mid, end)

    def merge(start, mid, end):
        temp = []
        lt, rt = start, mid

        while lt < mid and rt < end:
            if compare(lst[lt], lst[rt]) <= 0:
                temp.append(lst[lt])
                lt += 1
            else:
                temp.append(lst[rt])
                rt += 1
        while lt < mid:
            temp.append(lst[lt])
            lt += 1
        while rt < end:
            temp.append(lst[rt])
            rt += 1
        for i in range(start, end):
            lst[i] = temp[i - start]

    return sort(0, len(lst))


merge_sort(lst)
ans = []
for i in range(N):
    ans.append(f'{lst[i][0]} {lst[i][1]}')

print('\n'.join(ans))