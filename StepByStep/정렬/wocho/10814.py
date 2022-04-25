import sys
input = sys.stdin.readline

N = int(input())

members = []
for _ in range(N):
    temp = input().split()
    members.append((int(temp[0]), temp[1]))


def compare(a, b):
    return a[0] - b[0]

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

merge_sort(members)

ans = []
for i in range(N):
    ans.append(f'{members[i][0]} {members[i][1]}')

print('\n'.join(ans))
