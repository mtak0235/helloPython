import sys
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    lst.append(int(input()))


def merge_sort(arr):
    def sort(start, end):
        if end - start < 2:
            return
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        merge(start, mid, end)

    def merge(start, mid, end):
        lt = start
        rt = mid
        temp = []
        while lt < mid and rt < end:
            if arr[lt] <= arr[rt]:
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

    return sort(0, len(arr))


merge_sort(lst)

cnt = 0
common = []
i = 0
while i < N:
    j = i + 1
    while j < N:
        if lst[j] == lst[i]:
            j += 1
        else:
            break
    if cnt < j - i:
        common.clear()
        common.append(lst[i])
        cnt = j - i
    elif cnt == j - i:
        common.append(lst[i])
    i = j

print(round(sum(lst) / N))
print(lst[N // 2])
print(common[1] if len(common) > 1 else common[0])
print(lst[N - 1] - lst[0])
