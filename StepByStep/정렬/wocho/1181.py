import sys
input = sys.stdin.readline

N = int(input())

words = []
for _ in range(N):
    w = input().strip()
    words.append((w, len(w)))


def compare(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        for i in range(a[1]):
            if a[0][i] < b[0][i]:
                return -1
            elif a[0][i] > b[0][i]:
                return 1
        return 0
    return 1


def merge_sort(arr):
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
            if compare(arr[lt], arr[rt]) <= 0:
                temp.append(arr[lt])
                lt += 1
            else:
                temp.append(arr[rt])
                rt += 1
        while lt < mid:
            temp.append(arr[lt])
            lt += 1
        while rt < end:
            temp.append(arr[rt])
            rt += 1
        for i in range(start, end):
            arr[i] = temp[i - start]

    sort(0, len(arr))


merge_sort(words)

ans = [words[0][0]]
for i in range(1, N):
    if words[i - 1][0] != words[i][0]:
        ans.append(words[i][0])

print('\n'.join(ans))
